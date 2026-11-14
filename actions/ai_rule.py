#!/usr/bin/env python3
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from datetime import datetime, timezone
from ipaddress import ip_network
from typing import List, Set, Tuple

# > Dola（豆包海外版）：只维护这里，生成的规则始终置顶。
DOLA_RULES = [
    "DOMAIN-SUFFIX,dola.com",
    "DOMAIN-SUFFIX,ciciai.com",
    "DOMAIN-SUFFIX,ibyteimg.com",
    "DOMAIN-SUFFIX,byteintlapi.com",
]

RULE_SOURCES = [
    ("AI", "https://ddgksf2013.top/filter/Ai.yaml"),
    (
        "Apple Intelligence",
        "https://raw.githubusercontent.com/ddgksf2013/Filter/refs/heads/master/AppleIntelligence.list",
    ),
]

OUTPUT_FILES = ["lists/AI.list"]
README_PATH = "README.md"
HTTP_TIMEOUT_SECONDS = 60


def fetch_lines_from_url(url: str) -> List[str]:
    request = urllib.request.Request(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; AIRules/1.0; +https://github.com/uxudjs/Shadowrocket)"
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT_SECONDS) as response:
            status = getattr(response, "status", None)
            if status is not None and status != 200:
                raise RuntimeError(f"Unexpected HTTP status {status} for URL: {url}")
            text = response.read().decode("utf-8-sig")
    except (urllib.error.URLError, OSError, UnicodeError) as e:
        raise RuntimeError(f"Failed to fetch rules from {url}: {e}") from e
    if not text.strip():
        raise ValueError(f"Empty response from {url}")
    return text.splitlines()


def normalize_rule_line(line: str) -> str:
    parts = [part.strip() for part in line.split(",")]
    if len(parts) not in (2, 3) or not all(parts):
        raise ValueError(f"Invalid rule: {line!r}")

    rule_type = parts[0].upper()
    value = parts[1].lower()
    domain_types = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"}
    ip_types = {"IP-CIDR", "IP-CIDR6", "IP-ASN"}
    if rule_type not in domain_types | ip_types:
        raise ValueError(f"Unsupported rule type: {rule_type}")
    if len(parts) == 3 and (
        rule_type not in ip_types or parts[2].lower() != "no-resolve"
    ):
        raise ValueError(f"Unexpected policy or option in rule: {line!r}")

    if rule_type in domain_types:
        if not re.fullmatch(r"[a-z0-9_.-]+", value):
            raise ValueError(f"Invalid domain value: {value!r}")
    elif rule_type == "IP-ASN":
        if not value.isascii() or not value.isdecimal() or not 0 < int(value) <= 4294967295:
            raise ValueError(f"Invalid ASN: {value!r}")
    else:
        network = ip_network(value, strict=False)
        if "/" not in value or network.version != (4 if rule_type == "IP-CIDR" else 6):
            raise ValueError(f"Invalid network for {rule_type}: {value!r}")

    normalized = [rule_type, value]
    if len(parts) == 3:
        normalized.append("no-resolve")
    return ",".join(normalized)


def parse_source_lines(lines: List[str], yaml_payload: bool = False) -> List[str]:
    rules: List[str] = []
    has_payload = False
    for line_number, raw_line in enumerate(lines, start=1):
        line = raw_line.lstrip("\ufeff").strip()
        if not line or line.startswith(("#", ";", "!")):
            continue
        line = re.split(r"\s+#", line, maxsplit=1)[0].strip()
        try:
            if yaml_payload:
                if not has_payload:
                    if line != "payload:":
                        raise ValueError("Expected a YAML payload list")
                    has_payload = True
                    continue
                if not line.startswith("- "):
                    raise ValueError("Expected a YAML rule list item")
                line = line[2:].strip()
                if line.startswith(("'", '"')):
                    if len(line) < 2 or line[-1] != line[0]:
                        raise ValueError("Unclosed YAML rule string")
                    line = line[1:-1]
            rules.append(normalize_rule_line(line))
        except ValueError as e:
            raise ValueError(f"Line {line_number}: {e}") from e

    if not rules:
        raise ValueError("Source contains no valid rules")
    return rules


def merge_and_deduplicate_rules(
    source_rules: List[Tuple[str, List[str]]],
) -> List[Tuple[str, List[str]]]:
    unique_rules: Set[str] = set()
    merged_sources: List[Tuple[str, List[str]]] = []
    for index, (name, rules) in enumerate(source_rules):
        merged_rules: List[str] = []
        for rule in rules:
            if rule not in unique_rules:
                unique_rules.add(rule)
                merged_rules.append(rule)
        # Dola 保留手动顺序；上游各自排序，跨来源只去除完全相同的规则。
        if index > 0:
            merged_rules.sort()
        merged_sources.append((name, merged_rules))
    return merged_sources


def write_rules_to_file(
    sources: List[Tuple[str, List[str]]], output_path: str
) -> None:
    updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total_rules = sum(len(rules) for _, rules in sources)
    lines = [
        f"# Updated time: {updated_at}",
        f"# Total rules: {total_rules}",
        "# Thanks: ddgksf2013 and uxudjs",
        "",
    ]
    for name, rules in sources:
        if rules:
            lines.extend([f"# > {name}", *rules, ""])

    output_dir = os.path.dirname(output_path) or "."
    os.makedirs(output_dir, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=output_dir, delete=False
        ) as output:
            temporary_path = output.name
            output.write("\n".join(lines))
        os.replace(temporary_path, output_path)
    finally:
        if temporary_path is not None and os.path.exists(temporary_path):
            os.unlink(temporary_path)


def update_readme_rule_count(readme_path: str, total_rules: int) -> None:
    if not os.path.exists(readme_path):
        return
    with open(readme_path, "r", encoding="utf-8") as readme:
        content = readme.read()
    prefixes = [
        "AI合并规则总数：**",
        "AI合併規則總數：**",
        "AI merged rule count: **",
    ]
    for prefix in prefixes:
        content = re.sub(
            re.escape(prefix) + r"\d+\*\*",
            lambda match: prefix + str(total_rules) + "**",
            content,
        )
    with open(readme_path, "w", encoding="utf-8") as readme:
        readme.write(content)


def main() -> None:
    try:
        source_rules = [("Dola", parse_source_lines(DOLA_RULES))]
        for name, url in RULE_SOURCES:
            lines = fetch_lines_from_url(url)
            try:
                rules = parse_source_lines(lines, yaml_payload=url.endswith((".yaml", ".yml")))
            except ValueError as e:
                raise ValueError(f"Invalid rules from {url}: {e}") from e
            source_rules.append((name, rules))

        # 两个上游均获取并校验成功后才更新文件，避免用不完整的规则覆盖订阅。
        merged_sources = merge_and_deduplicate_rules(source_rules)
        total_rules = sum(len(rules) for _, rules in merged_sources)
        for path in OUTPUT_FILES:
            write_rules_to_file(merged_sources, path)
        update_readme_rule_count(README_PATH, total_rules)
        print(f"AI merged rule count: {total_rules}")
    except Exception as e:
        print(f"Error: failed to update AI rules: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
