"""
Content Chunker — splits parsed markdown into semantic chunks for embedding.

Chunks are:
1. Small enough for effective RAG retrieval (~500-1500 chars)
2. Aligned to H2 boundaries (## X.Y) where possible
3. Typed by their parent section (definition, formula, example, etc.)
4. Richly annotated with source metadata
"""
import hashlib
from dataclasses import dataclass, field

from alpnet.ingest.parser import ParsedFile


@dataclass
class Chunk:
    """A single content chunk ready for embedding."""
    chunk_id: str
    node_id: str                         # parent ParsedFile's node_id
    source_file: str                     # relative path
    content: str                         # markdown text
    chunk_type: str                      # "overview" | "definition" | "concept" | "formula" |
                                         # "graph" | "diagram" | "example" | "past_paper" |
                                         # "practical" | "concept_map" | "examiner" | "revision" | "metadata"
    section_number: int                  # which H1 section this chunk belongs to
    section_title: str                   # H1 section title
    h2_title: str                        # immediate H2 sub-heading
    metadata: dict = field(default_factory=dict)


SECTION_TYPE_MAP = {
    1: "overview",
    2: "syllabus",
    3: "definition",
    4: "concept",
    5: "formula",
    6: "graph",
    7: "diagram",
    8: "example",
    9: "past_paper",
    10: "practical",
    11: "concept_map",
    12: "examiner",
    13: "revision",
    14: "metadata",
}


class ContentChunker:
    """Splits ParsedFile content into embeddable Chunks."""

    MAX_CHUNK_LENGTH = 1500
    MIN_CHUNK_LENGTH = 200

    @classmethod
    def chunk_file(cls, parsed: ParsedFile, vault_root: str) -> list[Chunk]:
        """Chunk a single parsed file into semantic pieces."""
        chunks = []
        rel_path = str(parsed.file_path.relative_to(vault_root).parent
                       if hasattr(parsed.file_path, 'relative_to')
                       else parsed.node_id)

        for sec_num, section_content in parsed.sections.items():
            chunk_type = SECTION_TYPE_MAP.get(sec_num, "general")

            # Split section by H2 sub-headings
            sub_sections = cls._split_by_h2(section_content)

            for i, (h2_title, h2_content) in enumerate(sub_sections):
                # Skip very short or empty sections
                if len(h2_content.strip()) < cls.MIN_CHUNK_LENGTH:
                    continue

                # If content fits in one chunk, use it directly
                if len(h2_content) <= cls.MAX_CHUNK_LENGTH:
                    chunk = cls._make_chunk(
                        parsed, rel_path, sec_num, chunk_type, h2_title, h2_content, i
                    )
                    chunks.append(chunk)
                else:
                    # Split large sections by paragraph
                    sub_chunks = cls._split_long_content(
                        parsed, rel_path, sec_num, chunk_type, h2_title, h2_content
                    )
                    chunks.extend(sub_chunks)

        return chunks

    @staticmethod
    def _split_by_h2(content: str) -> list[tuple[str, str]]:
        """Split content by ## H2 headings. Returns list of (h2_title, content)."""
        import re
        h2_pattern = re.compile(r'^##\s+(.+)', re.MULTILINE)
        matches = list(h2_pattern.finditer(content))

        if not matches:
            # No H2 — treat entire content as one block
            return [("", content)]

        results = []
        for i, match in enumerate(matches):
            h2_title = match.group(1).strip()
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
            results.append((h2_title, content[start:end].strip()))

        return results

    @staticmethod
    def _split_long_content(
        parsed: ParsedFile,
        rel_path: str,
        sec_num: int,
        chunk_type: str,
        h2_title: str,
        content: str,
    ) -> list["Chunk"]:
        """Split overly long content by paragraph boundaries."""
        paragraphs = content.split("\n\n")
        chunks = []
        current = ""
        part = 0

        for para in paragraphs:
            if len(current) + len(para) < ContentChunker.MAX_CHUNK_LENGTH:
                current += ("\n\n" + para) if current else para
            else:
                if current.strip():
                    chunk = ContentChunker._make_chunk(
                        parsed, rel_path, sec_num, chunk_type,
                        h2_title, current.strip(), part
                    )
                    chunks.append(chunk)
                    part += 1
                current = para

        # Don't forget the last chunk
        if current.strip() and len(current.strip()) >= ContentChunker.MIN_CHUNK_LENGTH:
            chunk = ContentChunker._make_chunk(
                parsed, rel_path, sec_num, chunk_type,
                h2_title, current.strip(), part
            )
            chunks.append(chunk)

        return chunks

    @staticmethod
    def _make_chunk(
        parsed: ParsedFile,
        rel_path: str,
        sec_num: int,
        chunk_type: str,
        h2_title: str,
        content: str,
        index: int,
    ) -> Chunk:
        """Create a Chunk with a stable ID."""
        chunk_hash = hashlib.md5(content.encode()).hexdigest()[:12]
        chunk_id = f"{parsed.node_id}--s{sec_num}--{chunk_hash}"

        # Sanitize metadata for ChromaDB (no empty lists)
        safe_tags = parsed.tags if parsed.tags else ["untagged"]
        safe_syllabus = parsed.syllabus if parsed.syllabus else ["CAIE 9702"]
        safe_level = parsed.level or "AS"

        return Chunk(
            chunk_id=chunk_id,
            node_id=parsed.node_id,
            source_file=rel_path,
            content=content,
            chunk_type=chunk_type,
            section_number=sec_num,
            section_title=f"Section {sec_num}",
            h2_title=h2_title,
            metadata={
                "node_name": parsed.name,
                "node_type": parsed.node_type,
                "domain": parsed.domain,
                "level": safe_level,
                "difficulty": parsed.difficulty or "foundation",
                "tags": ",".join(safe_tags),
                "syllabus": ",".join(safe_syllabus),
            },
        )
