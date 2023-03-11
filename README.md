# hex-json
Convert [python dictionary | ASCII JSON string] into hexadecimal string.  
Restore from a hexadecimal string to [python dictionary | ASCII JSON string].  
Useful for ethereum transaction data signature.   

```no-highlight
https://github.com/Sobolev5/hex-json
```

## Install
To install run:
```no-highlight
pip install hex-json
```

### Convert and restore dict
```python
from hex_json import hex_serialize, hex_deserialize
d = {"hello": "world"}
hex_s = hex_serialize(d)
print(hex_s) # 0x10b9af5bde033362715ac3e14a8e3a374e572b9923e4d

d = hex_deserialize(hex_s)
print(d) # {'hello': 'world'}
print(type(d)) # <class 'str'>
```

### Convert and restore ASCII JSON string
```python
from hex_json import hex_serialize, hex_deserialize
d = '{"hello": "world"}'
hex_s = hex_serialize(d)
print(hex_s) # 0x389e07d8b54506b764401133595ffdc3b1729818953c64e47bc3ddbac98cea

d = hex_deserialize(hex_s)
print(d) # {"hello": "world"}
print(type(d)) # <class 'str'>
```

### Tests
```sh
tox
```