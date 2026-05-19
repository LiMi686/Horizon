#!/usr/bin/env python3
"""Send filtered daily summary email to subscribers (no papers)."""

import os
import re
import sys
import json
import smtplib
import markdown
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

# 爸爸邮件只保留这些来源关键词（白名单）
# 过滤掉：arXiv论文、签证、劳工局
EMAIL_EXCLUDED_KEYWORDS = ["arxiv", "arXiv", "immihelp", "Immigration", "Dept of Labor",
                           "visa", "National Immigration"]


def load_subscribers() -> list[str]:
    if not SUBSCRIBERS_FILE.exists():
        return []
    return json.loads(SUBSCRIBERS_FILE.read_text())


def filter_summary(text: str) -> str:
    """Keep only finance/AI/tech/health items for dad's email."""
    sections = re.split(r"\n---\n", text)
    filtered = [sections[0]]  # keep header

    for section in sections[1:]:
        # Skip items from excluded sources
        if any(kw in section for kw in EMAIL_EXCLUDED_KEYWORDS):
            continue
        filtered.append(section)

    # Rebuild and renumber the TOC
    body = "\n---\n".join(filtered)

    # Renumber the index list
    items = re.findall(r"^## \[(.+?)\]\(.+?\) ⭐️ ([\d.]+)/10", body, re.MULTILINE)
    new_toc = "\n".join(
        f"{i}. [{title}](#item-{i}) ⭐️ {score}/10"
        for i, (title, score) in enumerate(items, 1)
    )

    # Replace old TOC
    body = re.sub(
        r"(?m)^1\. \[.+?\n(?:^\d+\. \[.+?\n)*",
        new_toc + "\n",
        body,
        count=1,
    )

    # Update header count
    body = re.sub(
        r"From \d+ items, \d+ important",
        f"From many sources, {len(items)} important",
        body,
    )
    return body


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

    # Use Chinese summary only for email
    path = SUMMARIES_DIR / f"horizon-{target_date}-zh.md"
    if not path.exists():
        print(f"No summary found for {target_date}", file=sys.stderr)
        sys.exit(1)

    text = path.read_text(encoding="utf-8")
    filtered = filter_summary(text)

    subject = f"📰 科技日报 {target_date} | AI · 财经 · 健康"
    html = markdown.markdown(filtered, extensions=["tables"])

    # Wrap in simple styled HTML
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, sans-serif; max-width: 700px; margin: 0 auto; padding: 20px; color: #333; }}
  h1 {{ color: #1a1a2e; border-bottom: 2px solid #e8712a; padding-bottom: 8px; }}
  h2 {{ color: #16213e; font-size: 1.1em; margin-top: 24px; }}
  h3 {{ color: #0f3460; }}
  a {{ color: #e8712a; }}
  blockquote {{ border-left: 3px solid #e8712a; margin: 0; padding-left: 12px; color: #666; }}
  details {{ background: #f9f9f9; padding: 8px; border-radius: 4px; margin: 8px 0; }}
  hr {{ border: none; border-top: 1px solid #eee; margin: 24px 0; }}
</style>
</head><body>{html}</body></html>"""

    for subscriber in subscribers:
        try:
            send_email(subscriber, subject, html, filtered)
            print(f"  ✅ Sent to {subscriber}")
        except Exception as e:
            print(f"  ❌ Failed to send to {subscriber}: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
