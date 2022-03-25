# SimpleCFG

A library to easily manage program configuration, for Python.

## Installation

`pip install simplecfg`

## Quick Start

# // TODO: this

## Predefined Directories

SimpleCFG contains some predefined directories in the module `simplecfg.dir`,
to assist in configuration file placement. Each directory is accessed at
`simplecfg.dir.DIRNAME`

| Directory Name | Linux | Mac OS | Windows |
| --- | --- | --- | --- |
| `HOME` | `~` | `~` | `~` |
| `APP_DATA` | `~/.local/share` | `~\AppData\Roaming` | `~/Library/Application Support` |
| `CONFIG` | `~/.config` | `~\AppData\Roaming` | `~/Library/Application Support` |
| `TEMP` | `/tmp` | `~\AppData\Local\Temp` | `/tmp` |
