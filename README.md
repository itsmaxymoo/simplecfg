# SimpleCFG

A library to easily manage program configuration, for Python.

## Installation

`pip install simplecfg`

## Quick Start

```python
import simplecfg

cfg = simplecfg.Config("settings.cfg")

# Writing
cfg.set("username", "Max")
cfg["website"] = "https://itsmaxymoo.com"
cfg.write_file()

# Reading
cfg.read_file()
name = cfg.get("username") # 'name' contains "Max"
```

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
