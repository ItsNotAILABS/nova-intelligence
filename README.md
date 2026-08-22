# NOVA Intelligence

**Reusable intelligence contracts, compatibility review and evidence synthesis for the NEXUS ecosystem.**

NOVA Intelligence is the architecture/intelligence-contract plane. It turns research, runtime capability and model/system findings into structured plans, compatibility decisions and evidence objects that execution runtimes can consume.

```text
research / runtime state / requirements
              │
              ▼
       NOVA Intelligence
              │
              ├── capability review
              ├── compatibility analysis
              ├── plan review
              ├── research indexing
              ├── release-evidence classification
              └── bounded context / contract output
              │
              ▼
NEXUS route -> POCKET/Agent/Model/Worker execution
```

## NEXUS surface

[`ecosystem.surface.json`](ecosystem.surface.json) declares NOVA Intelligence to the federation.

Primary actions:

```text
intelligence.capabilities
compatibility.evaluate
release_evidence.classify
plan.review
research.index
```

NOVA Intelligence produces contracts, context and evidence; execution is delegated to the appropriate runtime plane.

## Practical uses

- review whether two repo/API protocol versions are compatible;
- inspect a proposed multi-component plan before execution;
- convert research findings into bounded implementation context;
- classify release evidence by source/test/package/deploy state;
- index architecture findings for later recall;
- detect contradictions between documentation, manifests and runtime declarations.

## Operating loop

```text
collect evidence
 -> normalize claim/capability
 -> compare against contract
 -> identify contradictions/gaps
 -> propose bounded next action
 -> emit context/evidence
 -> hand off to execution plane
```

## Ecosystem responsibilities

| System | Responsibility |
|---|---|
| NEXUS | canonical protocols, registry, routing |
| POCKET | identity, tenant, policy and product surfaces |
| NOVA Intelligence | contracts, compatibility, evidence and research synthesis |
| POCKET Agent | long-running execution |
| AURO / MESIE | model runtime and evaluation |
| Medina Memory | durable continuity |

## Verification

Validate local project tests plus the ecosystem declaration. From NEXUS:

```bash
python tools/validate_ecosystem_protocols.py
python tools/validate_ecosystem_registry.py
python tools/production_gate.py
```

## Production integration

Use NOVA Intelligence before execution when a request spans multiple versions, repositories, model/runtime capabilities or research claims. The output should be small enough to become a `nexus.context-pack.v1`, `nexus.compatibility.v1` or release-evidence object rather than a second hidden application state.

## Ecosystem

- [NEXUS](https://github.com/ItsNotAILABS/nexus)
- [POCKET](https://github.com/ItsNotAILABS/pocket)
- [POCKET Agent](https://github.com/ItsNotAILABS/pocket-agent)
- [AURO](https://github.com/ItsNotAILABS/AURO)
- [Medina Memory Systems](https://github.com/ItsNotAILABS/MedinaMemorySystems)

NOVA Intelligence is the system that asks: **what do we know, how strong is the evidence, what is compatible, and what should execute next?**
