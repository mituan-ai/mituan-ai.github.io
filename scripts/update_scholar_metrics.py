#!/usr/bin/env python3
"""Update homepage Google Scholar metrics through SerpAPI."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


AUTHOR_ID = "wIODRkYAAAAJ"
SERPAPI_ENDPOINT = "https://serpapi.com/search.json"
HOMEPAGE = Path(__file__).resolve().parents[1] / "content" / "_index.md"

METRIC_LABELS = {
    "works": "Publications and preprints",
    "citations": "Google Scholar citations",
    "h_index": "h-index",
    "i10_index": "i10-index",
}


def fetch_author(api_key: str) -> dict[str, Any]:
    query = urllib.parse.urlencode(
        {
            "engine": "google_scholar_author",
            "author_id": AUTHOR_ID,
            "hl": "en",
            "num": 100,
            "api_key": api_key,
        }
    )
    request = urllib.request.Request(
        f"{SERPAPI_ENDPOINT}?{query}",
        headers={"User-Agent": "mituan-ai-scholar-metrics/1.0"},
    )

    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"SerpAPI returned HTTP {error.code}") from None
    except urllib.error.URLError as error:
        raise RuntimeError(f"Could not reach SerpAPI: {error.reason}") from None
    except json.JSONDecodeError:
        raise RuntimeError("SerpAPI returned invalid JSON") from None

    if not isinstance(payload, dict):
        raise RuntimeError("SerpAPI returned an unexpected response")
    if payload.get("error"):
        raise RuntimeError(f"SerpAPI error: {payload['error']}")
    return payload


def _all_time_value(table: list[Any], aliases: tuple[str, ...]) -> int:
    for row in table:
        if not isinstance(row, dict):
            continue
        for alias in aliases:
            value = row.get(alias)
            if isinstance(value, dict) and isinstance(value.get("all"), int):
                return value["all"]
    raise RuntimeError(f"Missing Scholar metric: {aliases[0]}")


def extract_metrics(payload: dict[str, Any]) -> dict[str, int]:
    parameters = payload.get("search_parameters", {})
    response_author_id = parameters.get("author_id")
    if response_author_id and response_author_id != AUTHOR_ID:
        raise RuntimeError("SerpAPI returned data for a different Scholar author")

    articles = payload.get("articles")
    if not isinstance(articles, list):
        raise RuntimeError("SerpAPI response does not contain an article list")
    pagination = payload.get("serpapi_pagination", {})
    if isinstance(pagination, dict) and pagination.get("next"):
        raise RuntimeError("Scholar profile exceeds the 100-article safety limit")

    cited_by = payload.get("cited_by")
    table = cited_by.get("table") if isinstance(cited_by, dict) else None
    if not isinstance(table, list):
        raise RuntimeError("SerpAPI response does not contain citation metrics")

    return {
        "works": len(articles),
        "citations": _all_time_value(table, ("citations",)),
        "h_index": _all_time_value(table, ("h_index", "h-index")),
        "i10_index": _all_time_value(table, ("i10_index", "i10-index")),
    }


def update_homepage(metrics: dict[str, int], path: Path = HOMEPAGE) -> bool:
    content = path.read_text(encoding="utf-8")
    updated = content

    for metric, description in METRIC_LABELS.items():
        pattern = re.compile(
            rf'(?P<prefix>^\s*-\s+statistic:\s*)["\']?\d+["\']?'
            rf'(?P<suffix>\s*\n\s*description:\s*["\']{re.escape(description)}["\']\s*$)',
            flags=re.MULTILINE,
        )
        updated, count = pattern.subn(
            lambda match: (
                f'{match.group("prefix")}"{metrics[metric]}"{match.group("suffix")}'
            ),
            updated,
        )
        if count != 1:
            raise RuntimeError(
                f"Expected one homepage statistic for '{description}', found {count}"
            )

    if updated == content:
        return False
    path.write_text(updated, encoding="utf-8")
    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--fixture",
        type=Path,
        help="Read a local SerpAPI JSON response instead of calling the API.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.fixture:
            payload = json.loads(args.fixture.read_text(encoding="utf-8"))
        else:
            api_key = os.environ.get("SERPAPI_KEY", "").strip()
            if not api_key:
                raise RuntimeError("SERPAPI_KEY is not set")
            payload = fetch_author(api_key)

        metrics = extract_metrics(payload)
        changed = update_homepage(metrics)
    except (OSError, json.JSONDecodeError, RuntimeError) as error:
        print(f"Scholar update failed: {error}", file=sys.stderr)
        return 1

    state = "updated" if changed else "already current"
    print(
        "Scholar metrics "
        f"{state}: {metrics['works']} works, {metrics['citations']} citations, "
        f"h-index {metrics['h_index']}, i10-index {metrics['i10_index']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
