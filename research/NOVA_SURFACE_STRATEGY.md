# NOVA Surface Strategy

NOVA is the intelligence substrate. ChatGPT, Codex, CLIs, IDEs, SDKs, MCP servers, APIs, browser apps, and desktop shells are access surfaces.

This matters because the system should not collapse into "use ChatGPT as the brain." The correct architecture is:

```text
operator / user
  -> CLI, IDE, desktop, browser, ChatGPT app, API, SDK, MCP
  -> NOVA runtime
  -> MESIE, House law, proof ledger, model-run registry, deploy writer
  -> product output, code output, docs, packages, customer workflow
```

## Surface Roles

### CLI

The CLI is the fastest local operator lane. It should expose routing, terminal analysis, MESIE analysis, foundation runs, deploy checks, surface strategy, and proof inspection.

Current command:

```bash
python codex_cli.py surfaces
```

Next commands:

- `workspace open`
- `package verify`
- `mcp serve`
- `auth inspect`
- `proof tail`

### IDE / Workbench

The workbench is the Cursor-plus-Codex target: file tree, editor, diagnostics, preview, model/run comparison, deploy packaging, proof panel, and local file ingest.

NOVA owns the runtime state and proof. The editor is the control surface.

### Desktop App

The Electron app starts the local runtime, opens the platform, exposes a safe preload bridge, and packages into a native desktop app.

The renderer must never receive raw Node authority. The main process owns runtime process control.

### Apps SDK / MCP Inside ChatGPT

NOVA can become a ChatGPT app by exposing an MCP server and UI bundle. In that mode:

- ChatGPT is the host client.
- NOVA is the MCP/resource server.
- OAuth protects NOVA tools and user data.
- Tool calls must produce NOVA proof events.

This is not a way to embed the ChatGPT website or bypass API usage.

### Codex MCP Lane

Codex can be a coding specialist surface. It can authenticate with ChatGPT or API-key flows where OpenAI supports that, and it can connect to MCP servers.

NOVA should use Codex for repo-aware execution, review, patching, testing, and IDE workflows while preserving NOVA proof and permission boundaries.

### API Mode

API mode is for hosted products and third-party integrations. It needs:

- bearer token now
- OAuth/JWT roles next
- user/org database
- scoped permissions
- rate limits
- audit logs
- model-run replay and comparison
- consequence ledger integration

## Authorization Strategy

| Surface | Auth |
| --- | --- |
| Local CLI | OS user plus optional runtime token |
| Desktop | OS user, Electron main process, optional runtime token |
| Browser PWA | local runtime origin plus CORS boundary |
| ChatGPT App | OAuth to NOVA tools through Apps SDK/MCP |
| Codex CLI/IDE | OpenAI-supported ChatGPT sign-in, API key, or access token |
| Hosted API | bearer token now; OAuth/JWT roles next |
| Third-party SDKs | least-privilege OAuth/API secrets outside source |

## SDK Strategy

OpenAI Apps SDK belongs to the ChatGPT-native surface.

Responses API with remote MCP belongs to hosted product orchestration.

Agents SDK belongs to long-running multi-step workflows where NOVA owns state, approvals, and traces.

Codex CLI/IDE belongs to repo-aware software execution.

Third-party SDKs belong behind connector specs, permission scopes, fixtures, and proof gates.

## First Production Slice

1. Keep NOVA local runtime as the core.
2. Expose `/surfaces/strategy`.
3. Add `python codex_cli.py surfaces`.
4. Show the Surfaces view in the platform.
5. Package desktop source with Electron runtime control.
6. Build the NOVA MCP server package next.
7. Add OAuth metadata templates after MCP tools are stable.

## Monitor Next

- Create the NOVA MCP server package.
- Add OAuth metadata templates.
- Bind local file ingest to workbench editor tabs.
- Add task runner and terminal panel to the workbench.
- Add role-scoped auth and Cloudflare adapter.
- Add real connector specs for GitHub, Drive, Cloudflare, customer CRM, email, and construction bid workflows.
