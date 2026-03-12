#!/usr/bin/env python3
"""Malaysia health news fetcher.

Fetches health news from Malaysian news sources via RSS feeds.

Usage:
    uv run python scripts/fetchers/my_news.py

Output:
    data/news/latest_news.json
"""

import json
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Iterator

import feedparser
import requests
from bs4 import BeautifulSoup


@dataclass
class NewsItem:
    """A news item."""

    title: str
    url: str
    source: str
    published: str
    summary: str
    keywords_matched: list[str]


# Malaysian health news RSS feeds
NEWS_SOURCES = [
    {
        "name": "CodeBlue (Health News)",
        "url": "https://codeblue.galencentre.org/feed/",
        "category": "health",
    },
    {
        "name": "The Star Health",
        "url": "https://www.thestar.com.my/rss/News/Nation",
        "category": "general",
    },
    {
        "name": "New Straits Times",
        "url": "https://www.nst.com.my/rss",
        "category": "general",
    },
    {
        "name": "Malay Mail",
        "url": "https://www.malaymail.com/feed/rss/malaysia",
        "category": "general",
    },
    {
        "name": "Free Malaysia Today",
        "url": "https://www.freemalaysiatoday.com/rss/",
        "category": "general",
    },
]

# Health-related keywords for filtering general news
HEALTH_KEYWORDS = [
    # English
    "health", "medical", "medicine", "drug", "treatment", "therapy",
    "disease", "cancer", "diabetes", "hospital", "doctor", "patient",
    "pharmaceutical", "clinical", "trial", "vaccine", "virus",
    # Malay
    "kesihatan", "perubatan", "ubat", "rawatan", "penyakit", "hospital",
    "doktor", "pesakit", "vaksin", "kanser", "kencing manis",
]


def fetch_feed(url: str, timeout: int = 30) -> feedparser.FeedParserDict | None:
    """Fetch and parse an RSS feed.

    Args:
        url: Feed URL
        timeout: Request timeout in seconds

    Returns:
        Parsed feed or None on error
    """
    try:
        response = requests.get(url, timeout=timeout, headers={
            "User-Agent": "MyTxGNN News Monitor/1.0"
        })
        response.raise_for_status()
        return feedparser.parse(response.content)
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return None


def is_health_related(text: str) -> bool:
    """Check if text contains health-related keywords.

    Args:
        text: Text to check

    Returns:
        True if health-related
    """
    text_lower = text.lower()
    return any(kw in text_lower for kw in HEALTH_KEYWORDS)


def extract_matched_keywords(text: str, keywords: list[str]) -> list[str]:
    """Extract matched keywords from text.

    Args:
        text: Text to search
        keywords: Keywords to match

    Returns:
        List of matched keywords
    """
    text_lower = text.lower()
    matched = []
    for kw in keywords:
        if kw.lower() in text_lower:
            matched.append(kw)
    return matched


def clean_html(html: str) -> str:
    """Remove HTML tags from text.

    Args:
        html: HTML text

    Returns:
        Clean text
    """
    if not html:
        return ""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator=" ", strip=True)[:500]


def fetch_news(sources: list[dict], drug_keywords: list[str] = None) -> Iterator[NewsItem]:
    """Fetch news from all sources.

    Args:
        sources: List of news source configs
        drug_keywords: Optional list of drug keywords to match

    Yields:
        NewsItem objects
    """
    if drug_keywords is None:
        drug_keywords = []

    for source in sources:
        print(f"  Fetching from {source['name']}...")
        feed = fetch_feed(source["url"])

        if feed is None:
            continue

        for entry in feed.entries[:20]:  # Limit entries per source
            title = entry.get("title", "")
            summary = clean_html(entry.get("summary", entry.get("description", "")))
            text = f"{title} {summary}"

            # Filter general sources for health content
            if source["category"] == "general" and not is_health_related(text):
                continue

            # Extract matched keywords
            all_keywords = HEALTH_KEYWORDS + drug_keywords
            matched = extract_matched_keywords(text, all_keywords)

            # Parse date
            published = ""
            if hasattr(entry, "published_parsed") and entry.published_parsed:
                try:
                    published = datetime(*entry.published_parsed[:6]).isoformat()
                except Exception:
                    published = entry.get("published", "")
            else:
                published = entry.get("published", "")

            yield NewsItem(
                title=title,
                url=entry.get("link", ""),
                source=source["name"],
                published=published,
                summary=summary,
                keywords_matched=matched,
            )


def load_drug_keywords(path: Path) -> list[str]:
    """Load drug keywords from keywords.json.

    Args:
        path: Path to keywords.json

    Returns:
        List of drug names
    """
    if not path.exists():
        return []

    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    keywords = []
    for drug, info in data.get("drug_keywords", {}).items():
        keywords.append(drug)
        keywords.extend(info.get("synonyms", []))

    return keywords


def main():
    print("=" * 60)
    print("Fetching Malaysia Health News")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent.parent
    keywords_path = base_dir / "data" / "news" / "keywords.json"
    output_path = base_dir / "data" / "news" / "latest_news.json"

    # Load drug keywords
    print("1. Loading keywords...")
    drug_keywords = load_drug_keywords(keywords_path)
    print(f"   Loaded {len(drug_keywords)} drug keywords")

    # Fetch news
    print("2. Fetching news...")
    news_items = list(fetch_news(NEWS_SOURCES, drug_keywords))
    print(f"   Fetched {len(news_items)} health news items")

    # Save results
    print("3. Saving results...")
    output = {
        "fetched": datetime.now().isoformat(),
        "sources": [s["name"] for s in NEWS_SOURCES],
        "total_items": len(news_items),
        "items": [asdict(item) for item in news_items],
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print()
    print(f"News saved to: {output_path}")
    print()

    # Show sample
    if news_items:
        print("Sample news items:")
        for item in news_items[:5]:
            print(f"  - [{item.source}] {item.title[:60]}...")


if __name__ == "__main__":
    main()
