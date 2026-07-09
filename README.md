# NOVA Agent Council v0.8 — Production Layers

Local-first agent council for NOVA / ItsNotAILabs with MCP Spine, Gemini-compatible function declarations, repo intelligence, sandbox staging, D:\\ vault storage operations, HTML/Wasm-style capsules, ICP staging, and HERMES edge capsule staging.

## Start
```bat
Validate.bat
Start-NOVAAgentCouncil-MCP.bat
Start-NOVAAgentCouncil-Browser.bat
```

## Production gates
```bat
node scripts\validate.js
node engine\cli.js repo-index .
node adapters\gemini_adapter.js
node engine\cli.js capsule test-capsule
```

## Law
Agent tools discover and propose. Operator approval controls external action. Receipts prove the local work.
