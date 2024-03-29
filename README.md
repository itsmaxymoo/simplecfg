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

## Functions

All of the following functions are to be called on an instance of `simplecfg.Config`

| Name | Function | Argument(s) | Returns |
| --- | --- | --- | --- |
| `__init__(path: str)` | Constructor | Path to the config file | - |
| `get(key: str)` | Get an item from the config | Key name | Item stored at key, otherwise None |
| `set(key: str, value)` | Set a value in the config | Key name, item | None |
| `delete(key: str)` | Remove an item from the config | Key name | Item if found, otherwise None |
| `get_keys()` | Returns an iterable of all keys in the config | - | iterable |
| `dump()` | Returns text representation of the config | - | str |
| `wipe()` | Deletes all keys | - | - |
| `read_file(load_if_corrupt = False)` | Loads config from disk | Boolean to create an empty config if the file is corrupt. Otherwise, raise ValueError | - |
| `write_file()` | Commit config to disk | - | - |

### Magic Functions

| Name | Behavior |
| --- | --- |
| `__len__()` | Returns the number of keys in the config |
| `__contains__(key: str)` | Returns true if key exists in the config |
| `__getitem__(key: str)` | Alias to `get(key)` |
| `__setitem__(key: str, value)` | Alias to `set(key, value)` |
| `__delitem__(key: str)` | Alias to `delete(key)`, does not return anything |

## SynchronousConfig

Alternatively, you may opt to use `simplecfg.SynchronousConfig`.
It has the same functions as `simplecfg.Config`, but it will automatically
commit the config to disk with **every** modification.

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
