"""Repair content_md in knowledge_graph.json — replaces truncated content with full vault text."""
import json
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from alpnet.ingest.parser import MarkdownFileParser
from alpnet.db.graph_store import GraphStore
from alpnet.models.nodes import KnowledgeNode

VAULT_PATH = Path(__file__).resolve().parent.parent / "vault"
GRAPH_PATH = Path(__file__).resolve().parent.parent / "data" / "knowledge_graph.json"

def main():
    # Load existing graph
    store = GraphStore(GRAPH_PATH)
    graph = store.load()

    # Build a lookup: source_file -> node_id
    # source_file in graph is absolute path; we need to map back to vault relative path
    file_to_nodes: dict[str, list[str]] = {}
    for node_id, data in graph.nodes(data=True):
        sf = data.get("source_file", "")
        if sf:
            file_to_nodes.setdefault(sf, []).append(node_id)

    print(f"Found {len(file_to_nodes)} unique source files in graph")

    # Re-parse all vault files
    parsed_files = MarkdownFileParser.scan_vault(VAULT_PATH)
    print(f"Parsed {len(parsed_files)} vault files")

    # Build lookup: absolute path -> ParsedFile
    pf_by_path = {str(pf.file_path): pf for pf in parsed_files}

    updated = 0
    for abs_path, node_ids in file_to_nodes.items():
        pf = pf_by_path.get(abs_path)
        if not pf:
            # Try matching by suffix
            for p, pfile in pf_by_path.items():
                if p.endswith(abs_path) or abs_path.endswith(p):
                    pf = pfile
                    break
        if not pf:
            continue

        full_content = pf.content_md
        for nid in node_ids:
            old_len = len(graph.nodes[nid].get("content_md", "") or "")
            graph.nodes[nid]["content_md"] = full_content
            new_len = len(full_content)
            if new_len != old_len:
                updated += 1
                print(f"  Updated: {graph.nodes[nid].get('name', nid)} — {old_len} → {new_len} chars")

    print(f"\nUpdated {updated} nodes")

    # Save
    store.save()
    print(f"Graph saved to {GRAPH_PATH}")

    # Verify
    with open(GRAPH_PATH) as f:
        data = json.load(f)
    lengths = [len(n.get("content_md", "") or "") for n in data["nodes"]]
    print(f"\nVerification:")
    print(f"  Nodes: {len(data['nodes'])}")
    print(f"  Content lengths: min={min(lengths)}, max={max(lengths)}, avg={sum(lengths)//len(lengths)}")

if __name__ == "__main__":
    main()
