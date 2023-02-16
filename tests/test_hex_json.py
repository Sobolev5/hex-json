import os
import uuid
from hex_json import hex_serialize, hex_deserialize

def test():
    dicts = {uuid.uuid4().hex: uuid.uuid4().hex for x in range(50)}
    for d in dicts:
        hex_s = hex_serialize(d)
        restored_d = hex_deserialize(hex_s)
        assert d == restored_d