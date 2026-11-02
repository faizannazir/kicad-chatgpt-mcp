# KiCad MCP feature integration

The primary interactive design server is maintained in this repository. The Python analysis companion under `integrations/kicad-analysis-server/` is derived from the official upstream project maintained by **Seeed Studio**.

- **Original project:** [Seeed-Studio/kicad-mcp-server](https://github.com/Seeed-Studio/kicad-mcp-server)
- **Maintainer / original project owner:** [Seeed Studio](https://github.com/Seeed-Studio)
- **User's fork used as the integration source:** [faizannazir/kicad-mcp-server](https://github.com/faizannazir/kicad-mcp-server)
- **Imported source revision:** `0b445be8668c00b0d71315e74fa2f180bca686c2`
- **License declared in upstream pyproject.toml:** MIT

The companion adds hierarchical schematic and cross-sheet net analysis, pin-function and pin-conflict analysis, device-tree generation, embedded hardware-test templates, verified parts-registry search/download, PCB/schematic parsing, 3D/2D visualization exports, and native KiCad CLI ERC/DRC report parsing.

See [the companion setup guide](kicad-analysis-server/README.md) and [installation documentation](kicad-analysis-server/docs/INSTALLATION.md). Run it in its own Python environment and configure it as a second MCP server while its tools are validated. It is not yet registered inside the main TypeScript MCP process; this separation avoids duplicate tool names and Python dependency conflicts.

**Credit and provenance:** The companion is not original work authored by this repository. Preserve Seeed Studio's attribution and the upstream project URL in all redistributions and derivative releases. The user's fork is only the transfer/source branch; it is not the original project. See [UPSTREAM-NOTICE.md](kicad-analysis-server/UPSTREAM-NOTICE.md).
