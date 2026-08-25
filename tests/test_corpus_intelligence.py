from __future__ import annotations

from tools.corpus_intelligence import (
    classify_evidence,
    load_index,
    review_continuity,
    review_emergence,
    validate_index,
)


def test_full_corpus_index_is_valid():
    index = load_index()
    assert validate_index(index) == []
    assert len(index["papers"]) == 13


def test_source_cannot_satisfy_validated_deployment_claim():
    result = classify_evidence(
        claim_id="deployment:test",
        required_class="E3-validated-output",
        observed_class="E1-source",
        evidence=["repo:source"],
    )
    assert result["decision"] == "insufficient-evidence"


def test_continuity_requires_cross_session_or_cross_checkpoint_observation():
    result = review_continuity({
        "subject_id": "him",
        "checkpoint_id": "checkpoint-a",
        "memory_classes": ["working", "identity"],
        "observations": [{"same_session": True}],
        "receipt": {"sha256": "a" * 64},
    })
    assert result["review"] == "insufficient-evidence"
    assert any("same-session" in error for error in result["errors"])


def test_continuity_accepts_bounded_cross_checkpoint_candidate():
    result = review_continuity({
        "subject_id": "him",
        "checkpoint_id": "checkpoint-b",
        "memory_classes": ["identity", "procedural"],
        "observations": [{"cross_checkpoint": True, "evidence_ref": "artifact:continuity"}],
        "receipt": {"sha256": "b" * 64},
    })
    assert result["review"] == "admissible-candidate"


def test_emergence_review_rejects_novelty_without_recurrence_and_consequence():
    result = review_emergence({
        "observation_id": "obs-1",
        "subject": "auro",
        "window": {"start": 1, "end": 2},
        "subsystems": ["memory", "router"],
        "recurrence": [],
        "consequences": [],
        "novelty": {"score": 0.9},
        "evidence": ["artifact:novel-output"],
    })
    assert result["review"] == "insufficient-evidence"
    assert any("recurrence" in error for error in result["errors"])
