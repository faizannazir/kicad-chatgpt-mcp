# Installation and MCP client setup

This is the Python analysis companion derived from [Seeed Studio's original KiCad MCP Server](https://github.com/Seeed-Studio/kicad-mcp-server). The primary TypeScript KiCad editing server in the parent repository is a separate process.

## Requirements

- Python 3.10 or newer.
- KiCad 8 or newer; KiCad 9/10 is recommended.
- `kicad-cli` available on PATH for ERC/DRC and export operations.
- KiCad's `pcbnew` Python module for the full PCB API-backed analysis features. A normal system Python environment may not include it.

## Install

Run these commands from `integrations/kicad-analysis-server`.

### Windows (PowerShell)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m kicad_mcp_server
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
python -m kicad_mcp_server
```

The entry-point command is also available after installation:

```bash
kicad-mcp-server
```

## KiCad CLI

Check that KiCad CLI is available:

```bash
kicad-cli version
```

If it is not on PATH, set `KICAD_CLI` to the full executable path.

PowerShell:

```powershell
$env:KICAD_CLI = "C:\Program Files\KiCad\9.0\bin\kicad-cli.exe"
```

macOS example:

```bash
export KICAD_CLI="/Applications/KiCad/KiCad.app/Contents/MacOS/kicad-cli"
```

Linux example:

```bash
export KICAD_CLI="/usr/bin/kicad-cli"
```

The helper also searches PATH and common KiCad installation locations. Do not hard-code a path that does not match the installed KiCad version.

## Full PCB API support (`pcbnew`)

The companion can parse many files without importing `pcbnew`, but PCB API-backed operations need a Python interpreter that can import KiCad's own `pcbnew` module.

Check the interpreter:

```bash
python -c "import pcbnew; print(pcbnew.GetBuildVersion())"
```

If this fails, use the Python interpreter bundled with your KiCad installation or install the package into that interpreter. Typical locations:

- Windows: `C:\Program Files\KiCad\<version>\bin\python.exe`
- macOS: KiCad's bundled Python under `/Applications/KiCad/KiCad.app/Contents/Frameworks/`
- Linux: the system Python with the KiCad `pcbnew` bindings installed by the distribution.

Set `KICAD_PYTHON` to the interpreter path when the companion's automatic detection does not find it. Keep the MCP process and KiCad Python ABI compatible.

## Optional project configuration

Set `KICAD_PROJECT_PATHS` to a comma-separated list of permitted project directories. Other defaults are documented in `.env.example`.

Example:

```bash
KICAD_PROJECT_PATHS=/home/user/kicad-projects
```

Use absolute paths and only expose directories that the AI client is allowed to read or modify.

## MCP client configuration

The companion uses local stdio transport. Configure it as a second server alongside the primary TypeScript server. Example generic JSON entry:

```json
{
  "mcpServers": {
    "kicad-analysis": {
      "command": "/absolute/path/to/kicad-analysis-server/.venv/bin/python",
      "args": ["-m", "kicad_mcp_server"],
      "env": {
        "KICAD_CLI": "/absolute/path/to/kicad-cli",
        "KICAD_PROJECT_PATHS": "/absolute/path/to/kicad-projects"
      }
    }
  }
}
```

On Windows, use the full path to `.venv\Scripts\python.exe`. Remove environment entries you do not need. Keep project paths and executable paths specific to your machine. The exact configuration file location depends on the MCP client.

## Run tests

From this companion directory:

```bash
python -m pip install -e '.[test]'
python -m pytest tests/ -q
```

KiCad CLI integration tests skip when KiCad is not installed. The parser and hierarchy tests can run without a KiCad desktop session.

## Troubleshooting

- **`No module named pcbnew`:** use a KiCad-compatible Python interpreter or set `KICAD_PYTHON`. Static parser and CLI-backed features may still work without pcbnew.
- **`kicad-cli not found`:** set `KICAD_CLI` to the installed executable.
- **MCP server exits during startup:** run `python -m kicad_mcp_server` in the same environment and inspect the import error before configuring the client.
- **Permission denied:** grant access only to the intended project directory; avoid running the MCP server as Administrator/root.

## Safety

Always inspect generated files and run native KiCad ERC/DRC using a compatible KiCad version. Review footprints, symbol assignments, clearances, copper zones, stack-up, manufacturing outputs and electrical constraints before ordering boards. Generated firmware, device trees and tests are starting points, not hardware certification.
