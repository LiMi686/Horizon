#!/usr/bin/env python3
"""Push Horizon daily summary to Notion database."""

import os
import re
import sys
import httpx
from datetime import date
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = "359ff9ba-0cf9-819f-8bcf-f0f1ab6d0d57"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}
SUMMARIES_DIR = Path(__file__).parent.parent / "data" / "summaries"

# arXiv source names that count as "papers"
PAPER_SOURCES = {"arxiv", "arXiv", "paper"}


def rich_text(content: str) -> list[dict]:
    chunks = []
    for i in range(0, len(content), 2000):
        chunks.append({"type": "text", "text": {"content": content[i:i + 2000]}})
    return chunks or [{"type": "text", "text": {"content": ""}}]


def md_line_to_block(line: str) -> dict | None:
    line = line.rstrip()
    if not line or line == "---":
        return None
    if line.startswith("# "):
        return {"object": "block", "type": "heading_1",
                "heading_1": {"rich_text": rich_text(strip_md(line[2:]))}}
    if line.startswith("## "):
        return {"object": "block", "type": "heading_2",
                "heading_2": {"rich_text": rich_text(strip_md(line[3:]))}}
    if line.startswith("### "):
        return {"object": "block", "type": "heading_3",
                "heading_3": {"rich_text": rich_text(strip_md(line[4:]))}}
    if line.startswith("- ") or line.startswith("* "):
        return {"object": "block", "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": rich_text(strip_md(line[2:]))}}
    if re.match(r"^\d+\. ", line):
        text = re.sub(r"^\d+\. ", "", line)
        return {"object": "block", "type": "numbered_list_item",
                "numbered_list_item": {"rich_text": rich_text(strip_md(text))}}
    if line.startswith("> "):
        return {"object": "block", "type": "quote",
                "quote": {"rich_text": rich_text(strip_md(line[2:]))}}
    return {"object": "block", "type": "paragraph",
            "paragraph": {"rich_text": rich_text(strip_md(line))}}


def strip_md(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    return text.strip()


def md_to_blocks(md: str) -> list[dict]:
    return [b for line in md.splitlines() if (b := md_line_to_block(line))]


def append_blocks(page_id: str, blocks: list[dict]):
    for i in range(0, len(blocks), 100):
        resp = httpx.patch(
            f"https://api.notion.com/v1/blocks/{page_id}/children",
            headers=HEADERS,
            json={"children": blocks[i:i + 100]},
            timeout=60.0,
        )
        resp.raise_for_status()


def parse_header(text: str) -> tuple[int, int]:
    m = re.search(r"From (\d+) items.*?(\d+) important", text)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)


def parse_items(text: str) -> list[dict]:
    """Parse individual scored items from markdown summary."""
    items = []
    sections = re.split(r"\n---\n", text)
    for section in sections[1:]:
        title_m = re.search(r"^## \[(.+?)\]\((.+?)\)", section, re.MULTILINE)
        score_m = re.search(r"⭐️ ([\d.]+)/10", section)
        source_m = re.search(r"^(rss|reddit|hackernews|github) · (.+?) ·", section, re.MULTILINE)
        if title_m and score_m:
            source_line = source_m.group(0) if source_m else ""
            is_paper = any(p.lower() in source_line.lower() for p in PAPER_SOURCES) or \
                       "arxiv" in title_m.group(2).lower()
            items.append({
                "title": title_m.group(1),
                "url": title_m.group(2),
                "score": float(score_m.group(1)),
                "body": section.strip(),
                "is_paper": is_paper,
            })
    return items


def papers_section_blocks(papers: list[dict]) -> list[dict]:
    """Build Notion blocks for the top-3 papers callout section."""
    if not papers:
        return []

    blocks = [
        {"object": "block", "type": "divider", "divider": {}},
        {"object": "block", "type": "heading_2",
         "heading_2": {"rich_text": rich_text("📄 今日重磅论文 Top 3")}},
    ]

    for i, paper in enumerate(papers[:3], 1):
        score = paper["score"]
        title = paper["title"]
        url = paper["url"]

        # Numbered heading with score
        blocks.append({
            "object": "block", "type": "heading_3",
            "heading_3": {"rich_text": [
                {"type": "text", "text": {"content": f"{i}. {strip_md(title)} — ⭐️ {score}/10"}},
            ]},
        })

        # Extract summary / why_it_matters lines from the section body
        body = paper["body"]
        summary_lines = []
        for line in body.splitlines():
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("⭐") \
                    and not line.startswith("rss ·") and not line.startswith("reddit ·") \
                    and not line.startswith("hackernews ·") and "**标签**" not in line \
                    and not line.startswith("<") and not line.startswith("-"):
                summary_lines.append(line)
            if len(summary_lines) >= 3:
                break

        summary_text = " ".join(summary_lines)[:800] or "（详见正文）"
        blocks.append({
            "object": "block", "type": "paragraph",
            "paragraph": {"rich_text": rich_text(strip_md(summary_text))},
        })
        # Link as bookmark
        blocks.append({
            "object": "block", "type": "bookmark",
            "bookmark": {"url": url},
        })

    return blocks


def create_page(title: str, lang: str, target_date: str,
                all_items: int, important_items: int) -> tuple[str, str]:
    lang_label = "中文" if lang == "zh" else "English"
    payload = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "标题": {"title": [{"text": {"content": title}}]},
            "日期": {"date": {"start": target_date}},
            "语言": {"select": {"name": lang_label}},
            "来源数": {"number": all_items},
            "精选数": {"number": important_items},
        },
    }
    resp = httpx.post("https://api.notion.com/v1/pages", headers=HEADERS, json=payload)
    resp.raise_for_status()
    return resp.json()["id"], resp.json()["url"]


def main():
    if not NOTION_TOKEN:
        print("Error: NOTION_TOKEN not set in .env", file=sys.stderr)
        sys.exit(1)

    target_date = sys.argv[1] if len(sys.argv) > 1 else str(date.today())
    pushed = 0

    for lang in ["zh", "en"]:
        path = SUMMARIES_DIR / f"horizon-{target_date}-{lang}.md"
        if not path.exists():
            print(f"No {lang} summary for {target_date}, skipping.")
            continue

        text = path.read_text(encoding="utf-8")
        all_items, important_items = parse_header(text)
        items = parse_items(text)

        # Top 3 papers by score
        top_papers = sorted(
            [it for it in items if it["is_paper"]],
            key=lambda x: x["score"], reverse=True
        )[:3]

        title = f"Horizon {target_date} {'中文日报' if lang == 'zh' else 'Daily'}"
        print(f"Pushing {lang} ({important_items}/{all_items} items, {len(top_papers)} papers)...")
        page_id, url = create_page(title, lang, target_date, all_items, important_items)

        # Main content
        blocks = md_to_blocks(text)
        # Append papers section at the end
        blocks += papers_section_blocks(top_papers)

        append_blocks(page_id, blocks)
        print(f"  ✅ {url}")
        pushed += 1

    if not pushed:
        print(f"No summaries found for {target_date}.")
        sys.exit(1)


if __name__ == "__main__":
    main()
