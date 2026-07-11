#!/usr/bin/env python3
"""Validate the NOVA intelligence manifest and research packet.

This checker keeps the research library honest: listed papers must exist, the
manifest must declare proof gates, and the certification matrix must be present.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "nova-intelligence.manifest.json"
INDEX_PATH = ROOT / "research" / "RESEARCH_INDEX.md"
MATRIX_PATH = ROOT / "research" / "RESEARCH_CERTIFICATION_MATRIX.md"

PAPER_PATTERN = re.compile(r"`([^`]+\.md)`")


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in ("schema", "name", "authority", "repo_role", "runtime_surfaces", "proof_gates", "handoffs"):
        if field not in manifest:
            errors.append(f"manifest missing field: {field}")
    if not isinstance(manifest.get("runtime_surfaces"), list) or len(manifest.get("runtime_surfaces", [])) < 5:
        errors.append("manifest.runtime_surfaces must list at least five surfaces")
    if not isinstance(manifest.get("proof_gates"), list) or not manifest.get("proof_gates"):
        errors.append("manifest.proof_gates must be non-empty")
    packet = manifest.get("research_packet", {})
    if packet and packet.get("paper_count") != 10:
        errors.append("manifest.research_packet.paper_count should be 10 for this packet")
    return errors


def validate_research_index() -> list[str]:
    errors: list[str] = []
    if not INDEX_PATH.exists():
        return ["research/RESEARCH_INDEX.md is missing"]
    index_text = INDEX_PATH.read_text(encoding="utf-8")
    papers = [match for match in PAPER_PATTERN.findall(index_text) if match not in {"RESEARCH_INDEX.md", "RESEARCH_CERTIFICATION_MATRIX.md"}]
    unique_papers = sorted(set(papers))
    if len(unique_papers) != 10:
        errors.append(f"research index should list 10 unique papers, found {len(unique_papers)}")
    for paper in unique_papers:
        path = ROOT / "research" / paper
        if not path.exists():
            errors.append(f"listed paper is missing: research/{paper}")
    if not MATRIX_PATH.exists():
        errors.append("research/RESEARCH_CERTIFICATION_MATRIX.md is missing")
    return errors


def main() -> int:
    manifest = load_json(MANIFEST_PATH)
    errors = validate_manifest(manifest) + validate_research_index()
    if errors:
        print("NOVA research packet validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("NOVA research packet validation passed: 10 papers indexed with manifest proof gates")
    return 0


if __name__ == "__main__":
    sys.exit(main())
