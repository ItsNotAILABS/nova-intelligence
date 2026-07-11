# External AI Connector Platform

NOVA can connect to Caffeine CLI, Caffeine's MTP/MCP-style server surface, Grok Build, and future agent servers as worker surfaces. The rule is simple: external AIs can build, review, or package, but NOVA keeps the routing, proof gates, artifact import, and operator scope.

## Current Grounding

- Caffeine's documented local build path uses `@caffeineai/cli`, the `caffeine` command, and a loop through `auth login`, `doctor --fix`, `install`, `check --fix`, and `preview --build`.
- Caffeine apps use Motoko backend and React/Vite frontend conventions.
- Caffeine live publish should not be claimed as a local CLI action unless the current tool contract proves it.
- Grok Build is a terminal coding agent with plan/build/test/deploy workflow, skills, hooks, AGENTS.md, MCP servers, and headless/scriptable usage.
- Caffeine MTP/MCP is treated as configurable until the operator supplies the exact server URL and tool contract.

## Connectors

| Connector | Role | Boundary |
| --- | --- | --- |
| Caffeine CLI Bridge | Build Caffeine apps through local CLI workflow. | Auth and publish remain explicitly scoped. |
| Caffeine MTP/MCP Server Bridge | Register a server URL, discover tools, submit builds, import artifacts. | No assumed schema until tool discovery is captured. |
| Grok Build Bridge | Use Grok as external planning/build/review worker. | Plan, approval, diff, and test results must be captured. |
| Generic Agent Server Bridge | Future-proof adapter for agent task servers. | Requires schema, auth, timeout, and artifact hash. |

## Runtime Use

CLI:

```bash
PYTHONPATH=. python codex_cli.py connectors
PYTHONPATH=. python codex_cli.py connector-plan caffeine "build Motoko backend and React frontend"
PYTHONPATH=. python codex_cli.py connector-plan "caffeine mtp server" "send build request and import artifact"
PYTHONPATH=. python codex_cli.py connector-plan grok "review and patch checkout flow"
```

API:

```bash
curl -s http://127.0.0.1:8765/connectors/external-ai
curl -s http://127.0.0.1:8765/connectors/external-ai/plan \
  -H 'Content-Type: application/json' \
  -d '{"target":"caffeine mtp server","task":"send build request and import artifact"}'
```

Browser terminal:

```text
connector caffeine mtp server :: send build request and import artifact
```

## Monitor Next

The next build should create a `connector-run/` folder that stores discovery responses, task requests, imported artifact hashes, and verification reports for each external AI run.
