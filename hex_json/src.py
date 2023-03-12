import orjson
from typing import Any

def hex_serialize(payload: Any, *args, **kwargs) -> str:
    """
    Usage:
    import hex_json
    d = {"hello": "world"}
    hex_str = hex_json.hex_serialize(d)
    >>> 7b2268656c6c6f223a22776f726c64227d
    """
    
    assert bool(payload), "Empty payload"

    bytes_s = orjson.dumps(payload)
    return bytes_s.hex()

def hex_deserialize(s: str, *args, **kwargs) -> dict:
    """
    Usage:
    import hex_json
    s = "7b2268656c6c6f223a22776f726c64227d"
    d = hex_json.hex_deserialize(s)
    >>> {"hello": "world"}
    """
    
    assert isinstance(s, str), "Must be a string"
    assert bool(s), "Empty string"

    return orjson.loads(bytes.fromhex(s))
