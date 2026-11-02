# KiCad Analysis MCP Companion

This is a source-preserving import of `faizannazir/kicad-mcp-server` at commit `1adf313c6dc04f475abe85bc4aa67c102a59a4e5`. It complements the main TypeScript KiCad editing server with analysis and embedded-engineering workflows.

## Added capabilities

- Hierarchical schematic and cross-sheet net analysis.
- Netlist generation and pin-level tracing.
- MCU pin-function inference and pin-conflict checks.
- Device-tree generation for supported MCU families.
- Embedded hardware-test templates for Arduino, ESP-IDF, STM32 HAL, pytest and Unity.
- Search, inspect and download verified KiCad parts from a configurable parts registry.
- PCB/schematic file parsing, analysis and native CLI validation.

## Installation

Requires Python 3.10+ and KiCad CLI for native ERC/DRC workflows. From this directory:

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

For platform-specific setup and MCP client configuration, see `docs/INSTALLATION.md` (when present in this import) and the upstream setup instructions in the source repository.

## Use with the primary server

Run this companion as a separate MCP process alongside the main `kicad-chatgpt-mcp` server. This staged integration keeps tool names, dependencies and process lifecycles isolated while preserving all original code. A later integration can bridge selected analysis tools into the primary server after contract tests verify the tool schemas and runtime behavior.

## Validation and safety

- Parser success is not a substitute for KiCad's native ERC/DRC.
- Run native validation with a KiCad CLI version compatible with the project.
- Generated device trees and embedded tests are drafts requiring target-specific review.
- Review registry licenses and part provenance before using downloaded assets in a production library.
- MCP success does not imply electrical safety or manufacturing readiness.
