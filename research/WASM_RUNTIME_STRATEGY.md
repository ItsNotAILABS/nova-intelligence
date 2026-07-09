# NOVA Wasm Runtime Strategy

WebAssembly is the browser-native compute substrate for NOVA. It should not replace JavaScript UI code. It should accelerate bounded, CPU-heavy kernels where typed memory, predictable execution, and browser sandboxing matter.

## Verified Browser Runtime Model

Browser Wasm runtimes sit inside the major JavaScript engines:

- Chromium, Chrome, Edge, and Opera use V8.
- Firefox uses SpiderMonkey.
- Safari and WebKit-based browsers use JavaScriptCore.

The recommended fast loading path is `WebAssembly.instantiateStreaming()` when the server returns `application/wasm`. Fallback to `WebAssembly.instantiate()` with an `ArrayBuffer` when MIME or CSP prevents streaming.

## NOVA Placement

Wasm belongs under Substratum:

```text
Browser / Desktop PWA
  -> JavaScript UI and operator flow
  -> Web Worker boundary
  -> Wasm module for compute kernels
  -> proof event with module hash, feature probes, fallback route, and benchmark sample
```

## Good Fits

- MESIE spectral kernels
- FFT and signal processing
- image, video, and audio codecs
- cryptographic hashing
- simulation and physics
- large buffer parsing
- local ML inference kernels

## Poor Fits

- DOM-heavy UI
- small one-off functions
- workflows dominated by network waits
- arbitrary unreviewed native code
- threaded workloads without cross-origin isolation

## Feature Gates

- Streaming requires `application/wasm`.
- Threads require `SharedArrayBuffer` and cross-origin isolation through COOP/COEP headers.
- SIMD, relaxed SIMD, Memory64, GC, and JS string builtins should be feature-tested before production use.
- Browser WASI needs a JavaScript capability layer; do not assume native filesystem access.

## Production Rule

Every Wasm module shipped through NOVA needs:

- module SHA-256
- source language and compiler/toolchain note
- feature probe result
- JavaScript fallback
- benchmark against representative input
- runtime route: JS-only, Wasm-first, or hybrid JS UI plus Wasm worker kernel

## Current Implementation

Runtime module:

```text
codex_runtime/wasm_engine.py
```

API:

```text
GET  /wasm/manifest
POST /wasm/plan
```

CLI:

```bash
python codex_cli.py wasm "MESIE spectral FFT and matrix parsing"
```

Platform:

```text
NOVA Platform -> Wasm
```

## Sources

- MDN WebAssembly and JavaScript API reference
- WebAssembly.org feature status and Wasm 3.0 announcement
- V8 WebAssembly compilation pipeline
