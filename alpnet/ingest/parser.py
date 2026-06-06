"""
Markdown File Parser — parses .md files from the Obsidian vault.

Extracts:
- H1 sections (# 1. Title / 中文标题)
- All [[wikilinks]] with optional |alias
- YAML metadata from Section 14
- Node type detection (hub vs leaf vs sub-domain index)
- File hierarchy info (domain, subdomain, topic folder)
"""
import re
import yaml
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ParsedFile:
    """Result of parsing a single .md file."""
    file_path: Path
    node_id: str                          # unique slug from relative path
    name: str                             # display name (from H1 or filename)
    name_cn: str                          # Chinese name if found
    node_type: str                        # "topic_hub" | "leaf_concept" | "subdomain_index"
    domain: str                           # e.g., "01-Kinematics"
    subdomain: str                        # e.g., "01-Kinematics"
    topic_folder: str | None              # e.g., "Scalars and Vectors" (for hub + leaves)
    content_md: str                       # full raw markdown
    sections: dict[int, str]              # section_number -> raw markdown of that H1 section
    wikilinks: list[dict[str, str]]       # [{target, alias, section}]
    metadata: dict                        # parsed YAML from Section 14
    level: str                            # "AS" or "A2"
    difficulty: str                       # "foundation" | "intermediate" | "advanced"
    tags: list[str]
    syllabus: list[str]


class MarkdownFileParser:
    """Parses a vault markdown file into a structured ParsedFile."""

    H1_PATTERN = re.compile(r'^# (\d+)\.\s*(.+)', re.MULTILINE)
    WIKILINK_PATTERN = re.compile(r'\[\[([^\]|#]+?)(?:\|[^\]]+)?\]\]')
    YAML_BLOCK_PATTERN = re.compile(r'```yaml\n(.*?)\n```', re.DOTALL)

    @classmethod
    def parse(cls, file_path: Path, vault_root: Path) -> ParsedFile:
        content = file_path.read_text(encoding="utf-8")
        rel_path = file_path.relative_to(vault_root)

        # Determine hierarchy from path relative to vault root
        # Path: 01-Mechanics/01-Kinematics/TopicFolder/File.md
        #       parts[0]  parts[1]   parts[2]     parts[3]
        parts = rel_path.parts
        domain = parts[0] if len(parts) > 0 else ""
        subdomain, topic_folder, node_type = cls._detect_hierarchy(parts, file_path)

        # Extract sections
        sections = cls._extract_h1_sections(content)

        # Extract wikilinks (all of them, everywhere)
        wikilinks = []
        for match in cls.WIKILINK_PATTERN.finditer(content):
            target = match.group(1).strip()
            # Find which section this link is in
            sec_num = cls._find_section(content[:match.start()])
            wikilinks.append({"target": target, "alias": target, "section": sec_num})

        # Deduplicate wikilinks by target
        seen = set()
        unique_links = []
        for wl in wikilinks:
            key = wl["target"].lower()
            if key not in seen:
                seen.add(key)
                unique_links.append(wl)

        # Parse YAML metadata from Section 14 (handle malformed YAML in generated files)
        metadata = {}
        yaml_start_marker = content.rfind("```yaml")
        if yaml_start_marker >= 0:
            yaml_content_start = yaml_start_marker + 7
            yaml_end_marker = content.find("```", yaml_content_start)
            if yaml_end_marker < 0:
                yaml_text = content[yaml_content_start:]
            else:
                yaml_text = content[yaml_content_start:yaml_end_marker]
            yaml_text = yaml_text.strip()
            # Fix unquoted values containing colons (e.g., "WPH11 U1: 1.1-1.3")
            yaml_text = cls._fix_yaml_colons(yaml_text)
            try:
                metadata = yaml.safe_load(yaml_text) or {}
            except yaml.YAMLError:
                pass

        # Extract name from filename (the new format uses # 1. Overview as first H1, not a topic title)
        name = file_path.stem
        name_cn = ""
        first_line = content.strip().split("\n")[0]
        # Only use first line as name if it's a topic-level H1 (not a numbered section)
        if first_line.startswith("# ") and not cls.H1_PATTERN.match(first_line):
            full_title = first_line[2:].strip()
            name = full_title
            if " / " in full_title:
                parts_split = full_title.split(" / ", 1)
                name, name_cn = parts_split[0], parts_split[1]

        return ParsedFile(
            file_path=file_path,
            node_id=cls._make_node_id(rel_path),
            name=name,
            name_cn=name_cn,
            node_type=node_type,
            domain=domain,
            subdomain=subdomain,
            topic_folder=topic_folder,
            content_md=content,
            sections=sections,
            wikilinks=unique_links,
            metadata=metadata,
            level=metadata.get("level", ""),
            difficulty=metadata.get("difficulty", "foundation"),
            tags=metadata.get("tags", []),
            syllabus=metadata.get("syllabus", []),
        )

    @staticmethod
    def _fix_yaml_colons(yaml_text: str) -> str:
        """Quote YAML values that contain colons but aren't properly quoted.
        Handles both `key: value` lines and `- value` list items."""
        import re as _re
        fixed_lines = []
        for line in yaml_text.split('\n'):
            # Handle list items with colon in value: `  - Value: part`
            list_match = _re.match(r'^(\s*-\s)(.*)$', line)
            if list_match:
                prefix, value = list_match.groups()
                if value and ':' in value and not value.startswith(('"', "'", '[')):
                    value = f'"{value}"'
                fixed_lines.append(f'{prefix}{value}')
                continue
            # Handle inline list values with colons: `syllabus: [X: Y, Z]`
            inline_match = _re.match(r'^(\s*[\w-]+:\s)\[(.*)\]$', line)
            if inline_match:
                prefix, inner = inline_match.groups()
                # Quote each item in the list that contains a colon
                items = [item.strip() for item in inner.split(',')]
                quoted_items = [f'"{item}"' if ':' in item and not item.startswith('"') else item for item in items]
                fixed_lines.append(f'{prefix}[{", ".join(quoted_items)}]')
                continue
            # Handle plain key: value with colon in value
            match = _re.match(r'^(\s*[\w-]+:\s)(.*)$', line)
            if match:
                prefix, value = match.groups()
                if value and not value.startswith(('"', "'", '[', '{', '|', '>')):
                    if ':' in value and not value.startswith('- '):
                        value = f'"{value}"'
                fixed_lines.append(f'{prefix}{value}')
            else:
                fixed_lines.append(line)
        return '\n'.join(fixed_lines)

    @staticmethod
    def _detect_hierarchy(parts: tuple[str, ...], file_path: Path) -> tuple[str, str, str | None, str]:
        """
        Detect node type from file path relative to vault root.
        Path: 01-Mechanics/01-Kinematics/Scalars and Vectors/Scalars and Vectors.md
              parts[0] = domain, parts[1] = subdomain, parts[2] = topic_folder, parts[3] = filename
        """
        subdomain = parts[0] if len(parts) > 0 else ""
        topic_folder = None
        node_type = "leaf_concept"

        if len(parts) >= 4:
            # Full path: Domain/Subdomain/TopicFolder/File.md
            subdomain = parts[1]
            topic_folder = parts[2]
            file_stem = file_path.stem
            if file_stem == topic_folder:
                node_type = "topic_hub"
            else:
                node_type = "leaf_concept"
        elif len(parts) == 3:
            # Domain/Subdomain/File.md
            subdomain = parts[1]
            node_type = "subdomain_index"
            topic_folder = None
        else:
            subdomain = parts[0] if parts else ""

        return subdomain, topic_folder, node_type

    @classmethod
    def _extract_h1_sections(cls, content: str) -> dict[int, str]:
        """Extract H1 sections (# 1. Title) into a dict keyed by section number."""
        sections = {}
        matches = list(cls.H1_PATTERN.finditer(content))
        for i, match in enumerate(matches):
            sec_num = int(match.group(1))
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            sections[sec_num] = content[start:end].strip()
        return sections

    @classmethod
    def _find_section(cls, content_before: str) -> int:
        """Find which H1 section the given position belongs to."""
        matches = list(cls.H1_PATTERN.finditer(content_before))
        return int(matches[-1].group(1)) if matches else 0

    @staticmethod
    def _make_node_id(rel_path: Path) -> str:
        """Create a stable node ID from the relative path."""
        slug = str(rel_path.with_suffix("")).replace("/", "--").replace(" ", "-").lower()
        return slug

    @classmethod
    def scan_vault(cls, vault_root: Path) -> list[ParsedFile]:
        """Scan vault directory and parse all .md files."""
        results = []
        md_files = sorted(vault_root.glob("**/*.md"))
        for fp in md_files:
            # Skip .obsidian config and templates
            if ".obsidian" in fp.parts or "templates" in fp.parts:
                continue
            try:
                parsed = cls.parse(fp, vault_root)
                results.append(parsed)
            except Exception as e:
                print(f"  ⚠️  Parse error: {fp} — {e}")
        return results
