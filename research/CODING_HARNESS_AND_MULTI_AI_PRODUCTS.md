# Coding Harness and Multi-AI Modal Products

This release adds two product engines:

- **NOVA Coding Harness**: routes code work through intake, language/CPL routing, build, verification, packaging, and handoff.
- **NOVA Multi-AI Modal Product Suite**: defines product surfaces where multiple AI roles coordinate across code, files, documents, terminal, browser, memory, and protocol notation.

## Coding Harness

The harness does not treat coding as one command. It produces a proof-bearing build plan:

1. SENSUS Intake
2. Translatio Route
3. CORPUS Build
4. SVA Verify
5. SIGILLUM Package
6. MEMORIA Handoff

CLI:

```bash
PYTHONPATH=. python codex_cli.py harness
PYTHONPATH=. python codex_cli.py harness-plan "build C++ MESIE Wasm kernel and browser workbench"
```

API:

```bash
curl -s http://127.0.0.1:8765/coding-harness
curl -s http://127.0.0.1:8765/coding-harness/plan \
  -H 'Content-Type: application/json' \
  -d '{"intent":"build C++ MESIE Wasm kernel and browser workbench"}'
```

Browser terminal:

```text
harness build C++ MESIE Wasm kernel and browser workbench
```

## Multi-AI Modal Products

The product registry currently names:

- NOVABUILD Coding Harness
- AUTE Spec Launcher
- MERCATUS Outreach Studio
- MEMORIA Consequence Ledger
- CPL Protocol Foundry

Each product records modalities, AI roles, customer surface, workflow, proof gates, and launch endpoint.

CLI:

```bash
PYTHONPATH=. python codex_cli.py products
PYTHONPATH=. python codex_cli.py product-plan "customer outreach with compliance and consequence ledger"
```

API:

```bash
curl -s http://127.0.0.1:8765/multi-ai-products
curl -s http://127.0.0.1:8765/multi-ai-products/plan \
  -H 'Content-Type: application/json' \
  -d '{"request":"customer outreach with compliance and consequence ledger"}'
```

Browser terminal:

```text
product customer outreach with compliance and consequence ledger
```

## Monitor Next

The next hardening step is to make the harness create a `release-run/` folder containing `intake.json`, `route.json`, `verification.json`, `handoff.md`, and a signed proof manifest for each build.
