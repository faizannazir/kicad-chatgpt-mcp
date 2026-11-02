# KiCad Analysis MCP Companion

This companion is derived from the official [Seeed Studio KiCad MCP Server](https://github.com/Seeed-Studio/kicad-mcp-server), maintained by [Seeed Studio](https://github.com/Seeed-Studio). The source was obtained through the user's fork, [faizannazir/kicad-mcp-server](https://github.com/faizannazir/kicad-mcp-server), at revision `0b445be8668c00b0d71315e74fa2f180bca686c2`. See [UPSTREAM-NOTICE.md](UPSTREAM-NOTICE.md) for attribution and license details.

## Added capabilities

- Hierarchical schematic and cross-sheet net analysis.
- Netlist generation and pin-level tracing.
- MCU pin-function inference and pin-conflict checks.
- Device-tree generation for supported MCU families.
- Embedded hardware-test templates for Arduino, ESP-IDF, STM32 HAL, pytest and Unity.
- Search, inspect and download verified KiCad parts from a configurable parts registry.
- PCB/schematic parsing, PCB layout analysis and visualization exports.
- Native KiCad CLI ERC/DRC report execution and parsing.

## Installation

Requires Python 3.10+ and KiCad CLI. For full PCB analysis, install into the Python environment that can import KiCad's `pcbnew` module. Follow [docs/INSTALLATION.md](docs/INSTALLATION.md) for platform-specific setup.

From this directory:

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows PowerShell
# .venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m pip install -r requirements-test.txt
```

Run the companion:

```bash
kicad-mcp-server
```

## Use with the primary server

Run this companion as a separate MCP process alongside the main `kicad-chatgpt-mcp` server. This staged integration keeps tool names, dependencies and process lifecycles isolated while preserving the companion's independent runtime. The tools are not yet registered inside the primary TypeScript MCP process; do not describe them as native primary-server tools until that bridge is implemented and tested.

## Validation and safety

- Parser success is not a substitute for KiCad's native ERC/DRC.
- Run native validation with a KiCad CLI version compatible with the project.
- Generated device trees and embedded tests are drafts requiring target-specific review.
- Review registry licenses and part provenance before using downloaded assets in a production library.
- MCP success does not imply electrical safety or manufacturing readiness.
