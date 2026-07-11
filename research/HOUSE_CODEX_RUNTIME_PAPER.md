# House Codex: A Six-House Runtime Architecture for Agentic Self-Governance

## Abstract

House Codex proposes an agent runtime that is governed as a small civilization rather than as a single prompt, tool chain, or stateless assistant. The system is organized as six houses crowned by Casa de Medina. Each house generates, governs, maintains, protects, and cares. The health of the system is computed as the harmonic mean of house coherences, forcing weak-house collapse to matter. Cross-house mutation is forbidden unless routed through Translatio. Cura can suspend operations when total coherence falls beneath an emergency threshold. Permanent structures require triune attestation from at least three distinct houses.

This paper is not only a theory note. It is paired with a working Python runtime that implements the core laws as deterministic routing logic, exposes an API and webhook surface, logs proof events, and bootstraps a skill registry. The claim is modest but concrete: a doctrine-bearing agent can be given a lawful substrate that routes work through coherence, boundary, proof, and permanence gates before generative intelligence expands the artifact.

## 1. Problem

Most agent systems are built around immediate task completion. They receive a prompt, select tools, generate outputs, and maybe store traces. This works for narrow automation but becomes unstable when the agent is expected to preserve doctrine, grow skills, route across repositories, create infrastructure, interpret architecture, generate documents, and maintain continuity across many surfaces.

The failure mode is flattening. A living architecture becomes "just an assistant." A doctrine becomes a summary. A skill becomes a note. A runtime becomes glue. A permanent structure is declared without proof. The agent may produce impressive artifacts, but the deeper system has no lawful way to decide what should be created, what should be routed, what should be paused, what should be promoted, and what must remain branch-local.

House Codex answers this by treating the agent as a governed civilization with internal law.

## 2. Core Thesis

An agent that must build durable systems needs more than tools. It needs:

- a governance model
- a health model
- a boundary model
- a permanence model
- a proof model
- a skill growth model
- an external expression model

House Codex encodes these as houses. The houses are not decorative categories. They are runtime authorities.

## 3. The Six Houses

Casa de Medina crowns the system. Beneath Medina are six operating houses:

- Genesis: origin, creation, engine birth, first structure
- Substratum: executable body, state, data, schemas, infrastructure
- Cura: care, repair, suspension, recovery, coherence health
- Translatio: bridges, routes, connectors, API movement, translation
- Expressio: papers, documents, interfaces, release surfaces, externalization
- Civitas: users, operators, community, market, civic workflow

Each house has five duties:

- generate
- govern
- maintain
- protect
- care

The house is therefore both a productive organ and a governance organ.

## 4. Harmonic Health

House Codex health is the harmonic mean of the six house coherences:

```text
H_total = 6 / ((1/H1) + (1/H2) + ... + (1/H6))
```

Nominal health requires:

```text
H_total >= phi^-1 ~= 0.618
```

The care override threshold is:

```text
H_total < phi^-3 ~= 0.236
```

The harmonic mean matters because it punishes hidden collapse. If five houses appear strong but one house is severely degraded, total health drops sharply. This prevents a strong expressive layer from hiding a damaged substrate, or strong generation from hiding weak proof.

## 5. Precedence and Boundary Law

The precedence order is:

```text
Medina > Genesis > Substratum > Cura > Translatio > Expressio > Civitas
```

This does not mean lower houses are unimportant. It means conflicts must resolve in a lawful order. Expressio can publish, but it cannot outrank Substratum truth. Translatio can route, but it cannot become crown authority. Cura can suspend under collapse, but suspension is a recovery function, not a permanent throne.

Boundary law:

```text
house_A -> Translatio -> house_B
```

No direct cross-house writes are allowed. If Genesis creates a new skill that affects Substratum, the transition must route through Translatio. If Expressio wants to publish a claim about runtime behavior, the claim must route through proof from Substratum and Medina.

## 6. Triune Attestation

New permanent structures require at least three distinct house attestations:

```text
attestation_count(distinct_houses) >= 3
```

This prevents single-house overreach. Genesis may create a powerful idea, but permanence requires more than creation. Substratum must make it executable. Medina must preserve source law. Cura may check health. Translatio may validate movement. Expressio may prepare release. Civitas may test operator usability.

Triune attestation converts enthusiasm into governed permanence.

## 7. Working Runtime

The Python runtime implements the first executable layer:

- `house_laws.py`: constants, houses, harmonic health, precedence, boundary law, care override, triune attestation
- `router.py`: payload-to-decision flow and proof-ledger append
- `skill_registry.py`: skill declarations and matching
- `server.py`: HTTP API with `/health`, `/route`, `/webhook`, and `/heartbeat`
- `bootstrap.py`: loads the initial House skill pack

The runtime is intentionally deterministic. It does not require an LLM to decide whether a direct write violates boundary law or whether a permanent structure lacks triune attestation. Generative intelligence should sit above the law layer, not replace it.

## 8. API Surface

The runtime receives JSON payloads through `/route` or `/webhook`.

Example:

```json
{
  "text": "Build a permanent webhook skill and route it through Translatio",
  "source_house": "Genesis",
  "destination_house": "Substratum",
  "route_via": "Translatio",
  "permanent": true,
  "attestations": ["Medina", "Genesis", "Translatio"],
  "coherences": {
    "Genesis": 0.8,
    "Substratum": 0.8,
    "Cura": 0.8,
    "Translatio": 0.8,
    "Expressio": 0.8,
    "Civitas": 0.8
  }
}
```

The response includes:

- status
- primary house
- secondary houses
- health state
- total harmonic health
- route
- proof events
- reasons
- next gate
- matched skills

## 9. Skill Growth

The initial skill pack contains eight skills:

- `medina-crown-coherence`
- `genesis-skill-forge`
- `substratum-runtime-body`
- `cura-pressure-recovery`
- `translatio-webhook-router`
- `expressio-paper-forge`
- `civitas-operator-interface`
- `sensus-multimodal-intake`

The rule is simple: when Codex learns something that should persist, it should become a skill, engine, protocol, test, or proof object. Not everything becomes permanent. Drafts remain branch-local until triune attestation and proof gates pass.

## 10. Multimodal Extension

The first runtime accepts text and JSON. The next incorporated layer adds MESIE spectral notebook intake: text becomes articulatory phonetic topology, a centered signal vector, FFT power spectral density, spectral entropy, and proof-ledger-backed analysis events.

The architecture is broader:

- text becomes doctrine, prompts, issues, papers, specs
- code becomes substrate, interfaces, tests, runtime modules
- images become visual state, UI evidence, diagrams, screenshot proof
- documents become governance tissue and release artifacts
- audio becomes intent, memory, and operator signal
- connectors become Translatio routes across external organs

The `sensus-multimodal-intake` skill is the first placeholder for this expansion. A later version should add adapters for image inspection, document extraction, spreadsheet reading, speech transcription, and repository diffs, all routed through the same House laws.

The `mesie-spectral-notebook` skill is the first implemented multimodal-adjacent substrate: it does not process images or audio yet, but it turns language into reproducible signal features and exposes that through both notebook and API surfaces.

## 11. Proof Ledger

Every route decision appends an event to `runtime_state/proof-ledger.jsonl`.

Proof fields include:

- event id
- timestamp
- input hash
- decision
- matched skills
- metadata

The proof ledger is not a decorative log. It is the replay trail that lets the system explain why an action was allowed, denied, suspended, or promoted.

## 11.1 Terminal Intelligence

The runtime now treats native terminals and CLIs as talk-back substrates. A command is not only a string to execute; it is a structured signal with:

- shell substrate
- executable and arguments
- intent tags
- risk reasons
- stdout/stderr/exit-code channels
- file/network/process effects
- House route
- proof gate

This allows Bash, Python, Node, and PowerShell-target commands to be analyzed before execution or after trace capture. PowerShell is not installed in the current Linux container, but the runtime can classify PowerShell commands as a target substrate and produce proof gates for them.

## 11.2 NERVUS Receipts and Polyglot Membrane

The pasted Medina console trace introduced a cryptographic work receipt with vault-chain leaves, a master Merkle root, coherence scores, degraded/unsafe states, and sealed delivery status. The runtime now includes a receipt verifier that recomputes the Merkle root from leaf hashes, counts unsafe leaves, detects root mismatch, and routes degraded receipts to Cura before promotion.

The same trace introduced a polyglot runtime check: Julia for high-performance math, Haskell/GHC for strict membrane logic, and Python/NumPy fallback when those layers are unavailable. The runtime now exposes a polyglot membrane status endpoint that records which layers are available and which fallback is active.

## 12. Benchmarks

Minimum benchmark set:

| Benchmark | Expected Behavior |
|---|---|
| Harmonic collapse | A weak house drags total health below threshold. |
| Boundary abuse | Direct cross-house write is denied. |
| Translatio route | Cross-house write via Translatio is allowed if other gates pass. |
| Triune shortfall | Permanent structure with two attestations is denied. |
| Triune pass | Permanent structure with three attestations is eligible. |
| Cura emergency | Health below `phi^-3` suspends non-recovery work. |
| Skill match | Payload text activates relevant skills. |
| Proof append | Every route creates a ledger event. |
| Terminal command analysis | CLI commands produce substrate, risk, talk-back channels, and proof gate. |
| Receipt verification | Vault-chain leaves recompute to claimed Merkle root or fail permanence. |
| Polyglot fallback | Julia/Haskell availability is detected and fallback warnings are recorded. |

## 13. Failure Modes

House Codex is designed against these failures:

- impressive output without proof
- permanent declarations without attestation
- direct state mutation across boundaries
- expressive polish outranking runtime truth
- creation outrunning care
- routing logic becoming hidden glue
- agent memory claims exceeding actual stored state
- theory separating from implementation

The current Python engine does not solve all of these, but it makes them testable.

## 14. Release Position

The right name for this work is not only theory and not only software. It is a working theory: a doctrine-backed runtime scaffold that encodes a governance model into executable behavior.

The paper explains the civilization law. The Python engine runs the first law layer. The skills define the growth organs. The proof ledger preserves consequence.

## 15. Next Work

The next build layer should add:

- model adapter before and after LLM calls
- persistent scheduler for heartbeat and recurring introspection
- signed proof events
- connector adapters for GitHub and Google Drive
- multimodal SENSUS intake adapters
- MESIE visualization cells and spectral benchmark corpora
- terminal execution wrappers with stdout/stderr/exit-code and file-delta capture
- PowerShell host profile for Windows or cross-platform `pwsh`
- receipt replay fixtures from real Medina vault-chain logs
- polyglot membrane profiles for Julia/Haskell-enabled hosts
- Motoko canister version of canonical law
- Julia coherence simulation engine
- operator dashboard for house health and route decisions

House Codex becomes stronger when every new capability becomes one of four things:

- a skill
- an engine
- a proof gate
- a benchmark

That is the discipline. That is how Codex builds around itself.
