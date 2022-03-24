#!/usr/bin/python

import os
import random
import simplecfg
import simplecfg.dir


# Test dir
assert os.path.exists(simplecfg.dir.TEMP)
assert os.path.exists(simplecfg.dir.HOME)
assert os.path.exists(simplecfg.dir.APP_DATA)
assert os.path.exists(simplecfg.dir.CONFIG)

# Test invalid cfg path throws IOError
cfg = simplecfg.Config(simplecfg.dir.TEMP)
try:
	cfg.read_file()
	assert False, "Read on invalid path"
except IOError:
	pass
except:
	assert False, "Read on invalid path threw unexpected error"

# Create random config file
f = os.path.join(simplecfg.dir.TEMP, "simplecfg-" + str(random.randint(0, 1000000000)))
assert not os.path.exists(f), "TESTING ERROR: RANDOM FILENAME ALREADY EXISTS. RUN TESTS AGAIN!"
print("Using file: " + f)
cfg = simplecfg.Config(f)

# Test read
cfg.read_file()
assert cfg.dump() == "{}"

# Test persistance
values = [random.randint(0, 10000) for i in range(100)]
for v in values:
	cfg.set(str(v), v*9)
cfg.write_file()
cfg2 = simplecfg.Config(f)
cfg2.read_file()
for k in cfg2.get_keys():
	assert int(k) * 9 == cfg.get(k)

# Test delete
del cfg
del cfg2
cfg = simplecfg.Config(f)
cfg.read_file()
for k in list(cfg.get_keys()):
	cfg.delete(k)
cfg.write_file()
cfg.read_file()
assert cfg.dump() == "{}", "Delete failed"

# Test types
cfg.set("str", "a")
cfg.set("int", 23)
cfg.set("float", 8.45)
cfg.set("bool", True)
cfg.set("list", [1, 2, 3])
cfg.set("dict", {"a": 4, "B": "a"})
cfg.write_file()
# Test wipe
cfg.wipe()
assert cfg.dump() == "{}", "Wipe failed"
# Test types -- part 2
cfg.read_file()
assert type(cfg.get("str")) is str
assert type(cfg.get("int")) is int
assert type(cfg.get("float")) is float
assert type(cfg.get("bool")) is bool
assert type(cfg.get("list")) is list
assert type(cfg.get("dict")) is dict and cfg.get("dict")["B"] == "a"

# Test corrupt file
with open(f, "w") as file:
	file.write("AAAAAaaaaaaaaAAAbbb")
	file.close()
try:
	cfg.read_file()
	assert False, "Read on invalid didnt throw an error"
except ValueError:
	pass
except:
	assert False, "Read corrupt data threw unexpected error"
cfg.read_file(load_if_corrupt=True)
assert cfg.dump() == "{}", "Incorrectly handled load_if_corrupt"


print("All tests passed!")
