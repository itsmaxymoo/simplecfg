#!/usr/bin/python

import os
import random
import simplecfg

filename = "simplecfg-test-" + str(random.randint(0, 2000000000))
print("Attempting tests using file: " + os.path.join(simplecfg.dir.TEMP, filename))

# Ensure some built-in paths are valid
assert os.path.exists(simplecfg.dir.HOME), simplecfg.dir.HOME + " is NOT a valid path"
assert os.path.exists(simplecfg.dir.TEMP), simplecfg.dir.TEMP + " is NOT a valid path"

# Ensure config file gets created
c = simplecfg.Config(simplecfg.dir.TEMP, filename)
assert os.path.exists(os.path.join(simplecfg.dir.TEMP, filename)), "Config file not created"

# Test with random data
r1 = [
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000))),
	(str(random.randint(0, 2000000000)), str(random.randint(0, 2000000000)))
]
for d in r1:
	c.set(d[0], d[1])
for d in r1:
	v = c.get(d[0])
	assert v == d[1], "Key " + d[0] + " expects value \"" + d[1] + "\", instead got \"" + v + "\""
assert len(c.get_keys()) == 10, "Wrong number of keys in config"

# Test wipe
c.wipe()
assert c.get_keys() == [], "Wipe does not work"

# Test setting different data types
c.set("string", "test")
c.set("number", 13)
c.set("number2", 42.265)
c.set("bool", True)
c.set("list", ["a", "b", "c"])
c.set("dict", {
	"key1": "value1",
	"key2": 2,
	"key3": {"skey1": 10},
	"key4": [100, 2000]
})

# Ensure proper length
assert len(c.get_keys()) == 6, "Error setting other data types"

# Recall all other data types
assert c.get("string") == "test", "Error recalling proper string"
assert c.get("number") == 13, "Error recalling proper number"
assert c.get("number2") == 42.265, "Error recalling proper number (2)"
assert c.get("bool") == True, "Error recalling proper bool"
assert c.get("list") == ["a", "b", "c"], "Error recalling proper list"
assert c.get("dict") == {
	"key1": "value1",
	"key2": 2,
	"key3": {"skey1": 10},
	"key4": [100, 2000]
}, "Error recalling proper dict"

print("All tests passed!")
