#!/usr/bin/env python3
import sys
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone
from typing import List, Set

RULE_URLS = [
    "https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules.list",
    "https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge.txt"
]

OUTPUT_FILES = [
    "lists/fuck_ad_sr.list"
]

README_PATH = "README.md"

HTTP_TIMEOUT_SECONDS = 60

def fetch_lines_from_url(url: str) -> List[str]:
    if not isinstance(url, str) or not url:
        raise ValueError("URL must be a non-empty string")
    request = urllib.request.Request(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; FuckAD/1.0; +https://github.com/)"
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            status = getattr(response, "status", None)
            if status is not None and status != 200:
                raise RuntimeError(f"Unexpected HTTP status {status} for URL: {url}")
            raw_data = response.read()
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP error when fetching {url}: {e}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error when fetching {url}: {e}") from e
    except Exception as e:
        raise RuntimeError(f"Unknown error when fetching {url}: {e}") from e

    if raw_data is None:
        raise RuntimeError(f"Empty response when fetching {url}")

    text = ""
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            text = raw_data.decode(encoding)
            if text:
                break
        except UnicodeDecodeError:
            text = ""
            continue
    if not text:
        raise RuntimeError(f"Failed to decode response from {url} with common encodings")

    lines = text.splitlines()
    return lines

def is_comment_or_empty(line: str) -> bool:
    if line is None:
        return True
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith("#") or stripped.startswith(";") or stripped.startswith("!"):
        return True
    lower = stripped.lower()
    if lower.startswith("[adblock") or lower.startswith("[version") or lower.startswith("[filter"):
        return True
    return False

def normalize_rule_line(line: str) -> str:
    if line is None:
        return ""
    rule = line.strip()
    return rule

def merge_and_deduplicate_rules(multi_source_lines: List[List[str]]) -> List[str]:
    if not isinstance(multi_source_lines, list) or not multi_source_lines:
        raise ValueError("Input rule list must be a non-empty list of line lists")

    unique_rules: Set[str] = set()
    rules: List[str] = []

    for source_lines in multi_source_lines:
        if not isinstance(source_lines, list):
            continue
        for raw_line in source_lines:
            if not isinstance(raw_line, str):
                continue
            if is_comment_or_empty(raw_line):
                continue
            rule = normalize_rule_line(raw_line)
            if not rule:
                continue
            if rule in unique_rules:
                continue
            unique_rules.add(rule)
            rules.append(rule)

    rules.sort()
    return rules

def write_rules_to_file(rules: List[str], output_path: str) -> None:
    if not isinstance(output_path, str) or not output_path:
        raise ValueError("Output path must be a non-empty string")
    if rules is None:
        raise ValueError("Rules list must not be None")

    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total_rules = len(rules)

    header_lines = [
        f"# Updated time: {updated_at}",
        f"# Total rules: {total_rules}",
        "# Thanks: adrules.top and anti-ad.net",
        "",
    ]

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            for line in header_lines:
                f.write(line + "\n")
            for rule in rules:
                f.write(rule + "\n")
    except OSError as e:
        raise RuntimeError(f"Failed to write output file '{output_path}': {e}") from e

def update_readme_rule_count(readme_path: str, total_rules: int) -> None:
    if not isinstance(readme_path, str) or not readme_path:
        raise ValueError("Readme path must be a non-empty string")
    if not isinstance(total_rules, int) or total_rules < 0:
        raise ValueError("Total rules must be a non-negative integer")
    if not os.path.exists(readme_path):
        return
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return

    lines = content.splitlines()
    prefixes = [
        "FuckAd合并规则总数：**",
        "FuckAd合併規則總數：**",
        "FuckAd merged rule count: **"
    ]
    new_lines = []
    for line in lines:
        replaced = False
        for prefix in prefixes:
            idx = line.find(prefix)
            if idx != -1:
                after = line[idx + len(prefix):]
                end = after.find("**")
                if end != -1:
                    new_lines.append(line[:idx] + prefix + str(total_rules) + after[end:])
                    replaced = True
                    break
        if not replaced:
            new_lines.append(line)

    new_content = "\n".join(new_lines)
    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    except OSError:
        return

def main() -> None:
    all_source_lines: List[List[str]] = []

    for url in RULE_URLS:
        try:
            lines = fetch_lines_from_url(url)
        except Exception as e:
            print(f"Error: failed to fetch rules from {url}: {e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(lines, list):
            print(f"Error: invalid content fetched from {url}", file=sys.stderr)
            sys.exit(1)
        all_source_lines.append(lines)

    try:
        merged_rules = merge_and_deduplicate_rules(all_source_lines)
    except Exception as e:
        print(f"Error: failed to merge rules: {e}", file=sys.stderr)
        sys.exit(1)

    for path in OUTPUT_FILES:
        try:
            write_rules_to_file(merged_rules, path)
        except Exception as e:
            print(f"Error: failed to write output file '{path}': {e}", file=sys.stderr)
            sys.exit(1)

    try:
        update_readme_rule_count(README_PATH, len(merged_rules))
    except Exception:
        pass


if __name__ == "__main__":
    main()
