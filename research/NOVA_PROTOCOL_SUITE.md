# NOVA Multi-Communication Protocol Suite

NOVA should not build a one-off adapter for every business app. Business systems usually contain hundreds or thousands of surfaces. AI does not need a bespoke adapter for each one if the work is compressed into protocol families.

## Core Law

External systems enter NOVA through protocol families:

```text
External app / AI / service
  -> protocol family
  -> triple adapter face
  -> Latin organism agents
  -> task execution route
  -> proof and longevity state
```

## Triple Adapter Law

Every external capability should expose at least three faces when possible:

- MCP/tool contract
- HTTP/webhook resource
- CLI/SDK/operator command

This lets the same capability work inside ChatGPT apps, Codex, Claude/Cursor/Antigravity-style tools, terminal workflows, hosted APIs, and desktop builds.

## Latin Organism Agents

- `PONTIFEX`: bridge agent for MCP, APIs, CLIs, IDEs, and AI systems.
- `AURIGA`: route driver for task execution and protocol sequencing.
- `FABER`: builder agent for code, services, SDKs, and deploy packets.
- `CUSTOS`: permission, auth, risk, and boundary guard.
- `NUNTIUS`: multi-AI communication and handoff messenger.
- `MEMOR`: longevity, replay, consequence, and lineage memory.
- `TERMINUS`: NOVABUILD terminal execution face.
- `MERCATOR`: business workflow compression and customer app grouping.

## Protocol Families

- `PACTUM`: MCP service adapter protocol.
- `ORDO`: task execution protocol.
- `LEX`: routing and authority protocol.
- `MEMORIA`: longevity and continuity protocol.
- `FABRICA`: suite creation protocol.
- `PORTA`: IDE and collaboration protocol.
- `VIA`: external AI and tool protocol.
- `MERCATUS`: business app grouping protocol.

## Requested Stack Coverage

The suite groups the requested stack into reusable families:

- Ruby on Rails API
- Go Git Service
- MySQL
- Redis and Sidekiq
- Elasticsearch
- Kafka
- Kubernetes
- Go CLI
- TypeScript SDK
- CI/CD
- Rust Engine
- Python AI Service
- WebSockets / ActionCable / Yjs
- VS Code Extension
- LSP Protocol
- Antigravity
- Claude
- Grok
- Cursor
- NOVABUILD Terminal

## Runtime Hooks

```text
GET  /protocol-suite
POST /protocol-suite/route
```

CLI:

```bash
python codex_cli.py protocols
python codex_cli.py protocol-route "connect Antigravity Claude Grok Cursor Kafka VS Code into NOVABUILD"
```

Browser terminal:

```text
protocols
protocol connect Antigravity Claude Grok Cursor Kafka VS Code NOVABUILD terminal
```

## Production Rule

Actual connector implementations should come after the protocol contract is stable. The first release is intentionally read-only and route-planning oriented:

- group systems
- name auth boundaries
- name proof gates
- name runtime risks
- route intent through protocols and agents
- only then generate concrete service adapters
