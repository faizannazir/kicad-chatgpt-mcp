# Analysis MCP companion — integration boundary

The Python companion under `integrations/kicad-analysis-server` is derived from Seeed Studio's original project. It remains independently runnable.

## Why it is not yet bridged into the TypeScript server

The Python tools use FastMCP decorators and Python-specific schemas, while the primary server uses the TypeScript MCP SDK and Zod. There is no existing Python request protocol for analysis calls in the primary server. The current long-lived Python child is a different process and accepts KiCad editor scripting JSON commands on stdin; it is **not** a FastMCP stdio endpoint. Reusing it would mix two incompatible protocols and could corrupt responses.

## Safe bridge direction

Use a separate Python FastMCP child process launched as `python -m kicad_mcp_server`, with its own stdio pipes. The TypeScript server should:
- discover/list the companion's tools via MCP `tools/list`;
- register a small stable set of proxy tools or a single explicitly namespaced dispatch tool;
- call companion `tools/call` using MCP framing (not ad-hoc JSON lines);
- preserve structured content and surface errors/timeouts;
- terminate the child on server shutdown;
- avoid writing child stdout to the parent MCP stdout;
- validate paths against configured project roots before allowing file-reading/writing tools;
- never expose raw Python eval or arbitrary shell commands.

## Initial bridge scope

First proxy only read/analysis tools:
- hierarchical schematic/net analysis and connection tracing;
- pin-function analysis;
- component search;
- netlist generation/read/trace;
- PCB parsing/layout analysis;
- ERC/DRC run and report parsing (these invoke KiCad CLI and may write report files).

Do not proxy project creation, schematic editing, device-tree output, parts-registry downloads, or other write/network tools until permissions, output paths, and transaction behavior are defined.

## Validation checklist

- MCP initialize and tools/list handshake against a real FastMCP child.
- Correct JSON-RPC framing with partial/multiple stdout chunks.
- Request correlation and serialized writes.
- Timeout, child exit, malformed response, stderr logging and shutdown.
- Tool-name collision policy and namespaced descriptions.
- Read-only tools leave project files unchanged (except documented generated cache/report artifacts).
- Fixture-backed parser tests and native KiCad CLI tests where available.

This is a design boundary, not a claim that the proxy is implemented.
