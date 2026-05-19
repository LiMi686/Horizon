#!/usr/bin/env python3
"""Send filtered daily summary email to subscribers (no papers)."""

import os
import re
import sys
import json
import smtplib
from datetime import date
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465
EMAIL_ADDRESS = "lim33746@gmail.com"
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "")
SENDER_NAME = "科技日报 Horizon"

SUMMARIES_DIR = Path(__file__).parent.parent / "data" / "summaries"
SUBSCRIBERS_FILE = Path(__file__).parent.parent / "data" / "subscribers.json"

EMAIL_EXCLUDED_KEYWORDS = ["arxiv", "arXiv", "immihelp", "Immigration",
                           "Dept of Labor", "visa", "National Immigration"]


def load_subscribers() -> list[str]:
    if not SUBSCRIBERS_FILE.exists():
        return []
    return json.loads(SUBSCRIBERS_FILE.read_text())


def parse_items(text: str) -> list[dict]:
    """Parse items from markdown, return list of dicts."""
    items = []
    sections = re.split(r"\n---\n", text)
    for section in sections[1:]:
        if any(kw in section for kw in EMAIL_EXCLUDED_KEYWORDS):
            continue
        title_m = re.search(r"^## \[(.+?)\]\((.+?)\)", section, re.MULTILINE)
        score_m = re.search(r"⭐️ ([\d.]+)/10", section)
        if not title_m or not score_m:
            continue

        # Extract summary paragraph (first non-heading, non-empty line after ##)
        body_lines = []
        in_body = False
        for line in section.splitlines():
            if line.startswith("## "):
                in_body = True
                continue
            if not in_body:
                continue
            line = line.strip()
            if not line or line.startswith("rss ·") or line.startswith("reddit ·") \
                    or line.startswith("hackernews ·") or line.startswith("**") \
                    or line.startswith("<") or line.startswith("#"):
                continue
            body_lines.append(line)
            if len(body_lines) >= 2:
                break

        # Strip markdown links from summary
        summary = " ".join(body_lines)
        summary = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", summary)
        summary = re.sub(r"\*\*(.+?)\*\*", r"\1", summary)

        items.append({
            "title": title_m.group(1),
            "url": title_m.group(2),
            "score": float(score_m.group(1)),
            "summary": summary[:300],
        })
    return items


def build_html(items: list[dict], target_date: str) -> str:
    rows = ""
    for item in items:
        rows += f"""
        <tr>
          <td style="padding:16px 0; border-bottom:1px solid #f0f0f0;">
            <div style="font-size:13px; color:#999; margin-bottom:4px;">⭐️ {item['score']}/10</div>
            <div style="font-size:16px; font-weight:bold; margin-bottom:6px;">
              <a href="{item['url']}" style="color:#1a73e8; text-decoration:none;">{item['title']}</a>
            </div>
            <div style="font-size:14px; color:#555; line-height:1.6;">{item['summary']}</div>
            <div style="margin-top:8px;">
              <a href="{item['url']}" style="font-size:13px; color:#1a73e8;">{item['url']}</a>
            </div>
          </td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head>
<body style="margin:0;padding:0;background:#f5f5f5;font-family:Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f5f5f5;padding:20px 0;">
    <tr><td align="center">
      <table width="600" cellpadding="0" cellspacing="0" style="background:#fff;border-radius:8px;overflow:hidden;">
        <tr>
          <td style="background:#1a73e8;padding:24px 32px;">
            <div style="color:#fff;font-size:22px;font-weight:bold;">📰 科技日报</div>
            <div style="color:#aad4f5;font-size:14px;margin-top:4px;">{target_date} | AI · 财经 · 科技 · 健康</div>
          </td>
        </tr>
        <tr>
          <td style="padding:0 32px;">
            <table width="100%" cellpadding="0" cellspacing="0">
              {rows}
            </table>
          </td>
        </tr>
        <tr>
          <td style="padding:20px 32px;background:#f9f9f9;font-size:12px;color:#999;text-align:center;">
            由 Horizon AI 自动生成 · 每日北京时间 06:00 推送
          </td>
        </tr>
      </table>
    </td></tr>
  </table>
</body></html>"""


def build_plain(items: list[dict], target_date: str) -> str:
    lines = [f"科技日报 {target_date} | AI · 财经 · 科技 · 健康\n{'='*40}\n"]
    for i, item in enumerate(items, 1):
        lines.append(f"{i}. {item['title']} (⭐️{item['score']})")
        if item['summary']:
            lines.append(f"   {item['summary']}")
        lines.append(f"   链接：{item['url']}\n")
    return "\n".join(lines)


def send_email(to_addr: str, subject: str, html: str, plain: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"{SENDER_NAME} <{EMAIL_ADDRESS}>"
    msg["To"] = to_addr
    msg.attach(MIMEText(plain, "plain", "utf-8"))
    msg.attach(MIMEText(html, "html", "utf-8"))
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, to_addr, msg.as_string())


def main():
    if not EMAIL_PASSWORD:
        print("Error: EMAIL_PASSWORD not set", file=sys.stderr)
        sys.exit(1)

    target_date = sys.argv[1] if len(sys.argv) > 1 else str(date.today())
    subscribers = load_subscribers()
    if not subscribers:
        print("No subscribers found.")
        sys.exit(0)

    path = SUMMARIES_DIR / f"horizon-{target_date}-zh.md"
    if not path.exists():
        print(f"No summary found for {target_date}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    items = parse_items(text)
    print(f"  {len(items)} items after filtering")

    subject = f"📰 科技日报 {target_date} | AI · 财经 · 健康"
    html = build_html(items, target_date)
    plain = build_plain(items, target_date)

    for subscriber in subscribers:
        try:
            send_email(subscriber, subject, html, plain)
            print(f"  ✅ Sent to {subscriber}")
        except Exception as e:
            print(f"  ❌ Failed: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
