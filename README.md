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
print(hex_s) # 7b2268656c6c6f223a22776f726c64227d

d = hex_deserialize(hex_s)
print(d) # {'hello': 'world'}
print(type(d)) # <class 'str'>
```

### Convert and restore ASCII JSON string
```python
from hex_json import hex_serialize, hex_deserialize

s = '{"hello": "world"}'
hex_s = hex_serialize(s)
print(hex_s) # 227b5c2268656c6c6f5c223a205c22776f726c645c227d22

s = hex_deserialize(hex_s)
print(s) # {"hello": "world"}
print(type(s)) # <class 'str'>
```

### Tests
```sh
tox
```