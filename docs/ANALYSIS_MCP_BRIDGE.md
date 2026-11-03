## Bridge test plan

Keep the Python companion as a separate FastMCP process. The TypeScript server's existing Python child is the editor-script JSON-lines process; it is not FastMCP and must not be reused for analysis RPC.

Before implementing any proxy, cover: initialize/tools-list handshake; JSON-RPC framing across partial and multiple chunks; request IDs and serialized stdin; timeout and child-exit handling; stderr isolation; graceful shutdown; duplicate namespacing; path allow-listing; read-only tool side effects; native KiCad CLI integration; and malformed response handling.

Start with read/analysis tools only. Do not proxy project/schematic writes, registry downloads or generated output until explicit access and transaction boundaries exist.