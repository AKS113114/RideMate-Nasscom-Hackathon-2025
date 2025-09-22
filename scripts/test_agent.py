#!/usr/bin/env python3
"""
Validator for Inya.ai-style agent flow JSON.

Usage:
    python scripts/test_agent.py
"""

import json
import sys
from pathlib import Path

# ✅ File to validate
FLOW_PATH = Path("flows/Eco_Route_Handler.json")

def load_flow(path: Path):
    if not path.exists():
        print(f"❌ Flow file not found: {path}")
        sys.exit(2)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_flow(flow: dict):
    print("🔍 Validating Flow:", flow.get("name", "<unnamed>"))

    nodes = flow.get("nodesList", [])
    edges = flow.get("edgesList", [])

    print(f"Total Nodes: {len(nodes)}")
    print(f"Total Edges: {len(edges)}")

    # Check Start Node
    start_nodes = [n for n in nodes if n.get("type") == "START"]
    if start_nodes:
        print("✅ Start Node exists.")
    else:
        print("❌ No Start Node found!")

    # Check End Node (EVENT type with EOC/END/RESET)
    end_nodes = [
        n for n in nodes
        if n.get("type") == "EVENT" and n.get("eventNodeConfig", {}).get("eventType", "").upper() in ("EOC", "END", "RESET")
    ]
    if end_nodes:
        print("✅ End Node exists.")
    else:
        print("❌ No End Node found!")

    # Validate edge connections
    node_ids = {n.get("nodeId") for n in nodes}
    invalid_edges = []
    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        if src not in node_ids or tgt not in node_ids:
            invalid_edges.append(edge.get("edgeId", "<no-id>"))

    if invalid_edges:
        print("⚠️ Edges with invalid source/target:", invalid_edges)
    else:
        print("✅ All edges connect valid nodes.")

    # Check decision node usage
    decision_nodes = [n for n in nodes if n.get("type") == "DECISION"]
    if decision_nodes:
        print(f"ℹ️ Found {len(decision_nodes)} decision node(s). Ensure edge labels match decision outputs.")
    else:
        print("⚠️ No decision node found.")

    print("\n✅ Validation complete.")

if __name__ == "__main__":
    flow = load_flow(FLOW_PATH)
    test_flow(flow)
