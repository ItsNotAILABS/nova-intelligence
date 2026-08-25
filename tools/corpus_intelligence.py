#!/usr/bin/env python3
"""NOVA Intelligence review helpers for Corpus architecture v2.1.

The functions classify supplied evidence and inspect continuity/emergence
records. They do not execute tools, invent evidence, or promote checkpoints.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "research" / "corpus-index.json"
EVIDENCE_CLASSES = (
    "E0-assertion",
    "E1-source",
    "E2-execution-log",
    "E3-validated-output",
    "E4-signed-receipt",
    "E5-external-custody-and-reproduction",
)
MEMORY_CLASSES = (
    "weights", "working", "episodic", "semantic",
    "procedural", "relational", "identity",
)


def digest(value: Any) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str).encode("utf-8")
    ).hexdigest()


def load_index() -> dict[str, Any]:
    value = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise TypeError("research/corpus-index.json must be an object")
    return value


def validate_index(value: Mapping[str, Any] | None = None) -> list[str]:
    data = dict(value or load_index())
    errors: list[str] = []
    papers = data.get("papers") or []
    if data.get("schema") != "nova.corpus-research-index.v1":
        errors.append("unexpected research-index schema")
    if [item.get("number") for item in papers] != list(range(1, 14)):
        errors.append("paper numbers must be ordered 1..13")
    if len({item.get("id") for item in papers}) != 13:
        errors.append("paper IDs must be unique")
    if tuple(data.get("evidence_classes") or ()) != EVIDENCE_CLASSES:
        errors.append("evidence classes must preserve E0-E5 order")
    if tuple(data.get("memory_classes") or ()) != MEMORY_CLASSES:
        errors.append("memory classes differ from canonical order")
    if len(data.get("claim_boundaries") or []) != 8:
        errors.append("all eight claim boundaries are required")
    return errors


def evidence_rank(value: str) -> int:
    try:
        return EVIDENCE_CLASSES.index(value)
    except ValueError as exc:
        raise ValueError(f"unknown evidence class: {value}") from exc


def classify_evidence(
    *,
    claim_id: str,
    required_class: str,
    observed_class: str,
    evidence: Sequence[str],
) -> dict[str, Any]:
    refs = [str(item) for item in evidence if str(item).strip()]
    sufficient = evidence_rank(observed_class) >= evidence_rank(required_class)
    if observed_class != "E0-assertion" and not refs:
        sufficient = False
    payload = {
        "schema": "nexus.evidence-classification.v1",
        "claim_id": claim_id,
        "required_class": required_class,
        "observed_class": observed_class,
        "evidence": refs,
        "decision": "supported" if sufficient else "insufficient-evidence",
        "observed_at": "runtime-generated",
    }
    payload["classification_sha256"] = digest(payload)
    return payload


def review_continuity(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    missing = [field for field in ("subject_id", "checkpoint_id", "memory_classes", "observations", "receipt") if field not in snapshot]
    observations = list(snapshot.get("observations") or [])
    observed_classes = set(snapshot.get("memory_classes") or [])
    cross_session = any(bool(item.get("cross_session")) for item in observations if isinstance(item, Mapping))
    cross_checkpoint = any(bool(item.get("cross_checkpoint")) for item in observations if isinstance(item, Mapping))
    errors = [f"missing field: {field}" for field in missing]
    unknown = sorted(observed_classes - set(MEMORY_CLASSES))
    if unknown:
        errors.append(f"unknown memory classes: {unknown}")
    if not (cross_session or cross_checkpoint):
        errors.append("same-session observations do not establish durable continuity")
    result = {
        "schema": "nexus.continuity-snapshot.v1",
        "subject_id": snapshot.get("subject_id"),
        "checkpoint_id": snapshot.get("checkpoint_id"),
        "memory_classes": sorted(observed_classes),
        "observations": observations,
        "receipt": snapshot.get("receipt"),
        "created_at": snapshot.get("created_at", "runtime-generated"),
        "review": "admissible-candidate" if not errors else "insufficient-evidence",
        "errors": errors,
        "claim_boundary": "continuity review does not promote a checkpoint or prove consciousness",
    }
    result["review_sha256"] = digest(result)
    return result


def review_emergence(observation: Mapping[str, Any]) -> dict[str, Any]:
    required = ("observation_id", "subject", "window", "subsystems", "recurrence", "consequences", "novelty", "evidence")
    errors = [f"missing field: {field}" for field in required if field not in observation]
    if not observation.get("subsystems"):
        errors.append("at least one subsystem is required")
    if not observation.get("recurrence"):
        errors.append("recurrence evidence is required")
    if not observation.get("consequences"):
        errors.append("consequence evidence is required")
    if not observation.get("evidence"):
        errors.append("novelty without evidence is insufficient")
    result = {
        "schema": "nexus.emergence-observation.v1",
        **{field: observation.get(field) for field in required},
        "review": "bounded-longitudinal-candidate" if not errors else "insufficient-evidence",
        "errors": errors,
        "claim_boundary": "the observation does not establish consciousness, sentience, or unrestricted autonomy",
    }
    result["review_sha256"] = digest(result)
    return result


def main() -> int:
    index = load_index()
    errors = validate_index(index)
    report = {
        "schema": "nova.corpus-index-validation.v1",
        "corpus": index.get("corpus"),
        "paper_count": len(index.get("papers") or []),
        "status": "pass" if not errors else "fail",
        "errors": errors,
    }
    report["receipt_sha256"] = digest(report)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
