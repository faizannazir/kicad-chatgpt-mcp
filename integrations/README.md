# KiCad MCP feature integration

The `kicad-chatgpt-mcp` project remains the primary interactive design server. The additional Python analysis server is integrated under `integrations/kicad-analysis-server/` as a separately runnable companion, preserving its FastMCP implementation and its own dependency set.

The companion adds hierarchical schematic analysis, cross-sheet net tracing, pin-function and pin-conflict analysis, device-tree generation, embedded hardware test templates, verified parts-registry search/download, file-based PCB analysis, and native KiCad CLI ERC/DRC report parsing.

See `kicad-analysis-server/README.md` and `kicad-analysis-server/docs/INSTALLATION.md` for setup. Run it in its own virtual environment. Configure it as a second MCP server in your client while the integration is validated. Tools are not yet registered in the main TypeScript MCP process; keeping the boundary explicit avoids duplicate tool names and Python dependency conflicts.

The integration retains the source project's MIT declaration and upstream contributor history in its imported source files. The import is pinned to upstream commit `1adf313c6dc04f475abe85bc4aa67c102a59a4e5`. Review upstream changes before updating.
