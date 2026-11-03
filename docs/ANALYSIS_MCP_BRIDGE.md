# KiCad Analysis Companion Bridge — Engineering Notes

The Python companion remains a separate FastMCP process; it is not the editor scripting child.

## Current integration state

- Main KiCad server: TypeScript MCP SDK, direct tools, plus a legacy Python child that receives editor commands as newline-delimited JSON.
- Analysis companion: FastMCP Python, separate MCP stdio protocol and own tool catalog.
- Do not route companion JSON-RPC through the legacy editor child or merge both stdout streams into the parent's MCP stdout.

## Read-only candidate inventory

Candidate tools for a first proxy release:
- `analyze_hierarchical_nets`, `trace_hierarchical_connection`
- `analyze_pin_functions`, `detect_pin_conflicts`
- `search_components_by_type`
- `get_netlist_nets`, `get_netlist_components`, `trace_netlist_connection`
- `list_pcb_footprints`, `get_pcb_statistics`, `analyze_pcb_nets`, `find_tracks_by_net`
- `get_erc_violations`, `get_drc_violations`
- `get_schematic_info`, `list_schematic_components`, `list_schematic_nets`

Caveats: netlist and ERC/DRC calls can invoke KiCad CLI and write temp cache/report artifacts. Treat them as project-read operations with documented side effects—not pure filesystem reads. Do not expose report exports, registry downloads, project/schematic writes, device-tree generation or PCB layout generation in the first bridge.

## Implementation contract

Use an independent child process started with the configured companion interpreter and `-m kicad_mcp_server`. Implement MCP JSON-RPC framing with Content-Length headers (or the exact transport used by the pinned FastMCP/MCP SDK), initialize handshake, `tools/list`, and `tools/call`. Do not assume newline-delimited JSON.

- One serialized writer and a parser that handles fragmented/multiple frames.
- Correlate responses by request ID; reject unknown IDs.
- stderr is logs only; stdout is protocol only.
- Timeout, process exit, malformed JSON, protocol error and shutdown all reject pending requests cleanly.
- Namespaced public tools (`analysis__...`) to prevent collisions with primary tools.
- Validate source paths against configured allow-listed project roots; reject traversal and symlink escapes.
- Limit output size and avoid leaking arbitrary local file paths beyond the authorized roots.
- Close child gracefully, then terminate on timeout.

## Required tests before release

1. Unit test Content-Length frame parser: fragmented header/body, multiple frames, invalid length, oversized frame.
2. Fake child test: initialize, list, call; fragmented response; stderr chatter; out-of-order IDs; child exit; timeout; malformed frame.
3. Tool registration test: namespaces, stable names/descriptions, schemas preserved, no accidental duplicate names.
4. Path policy tests: allowed root, sibling escape, `..`, symlink escape, Windows drive/UNC.
5. Integration test against actual FastMCP child (Python environment with companion extras).
6. Optional KiCad CLI integration tests on supported KiCad version.

Do not mark bridged analysis tools as available until this contract passes.
