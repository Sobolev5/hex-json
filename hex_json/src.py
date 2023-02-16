from textwrap import wrap
import orjson


def hex_serialize(_: dict, *args, **kwargs) -> str:
    """
    Usage:
    import hex_json
    d = {"hello": "world"}
    hex_str = hex_json.hex_serialize(d)
    >>> 0x10b9af5bde033362715ac3e14a8e3a374e572b9923e4d
    """

    # check
    assert (isinstance(_, dict) or isinstance(_, str)) == True, "Must be a dictionary or string"
    assert bool(_) == True, "Empty dictionary or string"

    # convert
    bytes_s = orjson.dumps(_)
    unicode_nums = ["100"]  
    for unicode_num in bytes_s:
        if unicode_num < 10:
            unicode_num = "00%s" % unicode_num
        elif unicode_num < 100:
            unicode_num = "0%s" % unicode_num
        else:
            unicode_num = "%s" % unicode_num
        unicode_nums.append(unicode_num)
    chars_to_int = int("".join(unicode_nums))
    return hex(chars_to_int)


def hex_deserialize(s: str, *args, **kwargs) -> dict:
    """
    Usage:
    import hex_json
    s = "0x10b9af5bde033362715ac3e14a8e3a374e572b9923e4d"
    d = hex_json.hex_deserialize(s)
    >>> {'hello': 'world'}
    """

    # check
    assert isinstance(s, str) == True, "Must be a string"
    assert bool(s) == True, "Empty string"

    # convert
    hex_to_int = str(int(s, 16))
    unicode_nums = wrap(hex_to_int, 3)
    chars = []
    for i, unicode_num in enumerate(unicode_nums, start=1):
        if i == 1:
            if unicode_num == "100":
                continue
            else:
                raise TypeError('Invalid start character num (must be 100)')
        if unicode_num[0:2] == "00":
            unicode_num = unicode_num[2:]
        elif unicode_num[0] == "0":
            unicode_num = unicode_num[1:]
        try:
            chars.append(chr(int(unicode_num)))
        except:
            raise TypeError(f'Error due converting unicode_num={unicode_num}')
    return orjson.loads("".join(chars))
