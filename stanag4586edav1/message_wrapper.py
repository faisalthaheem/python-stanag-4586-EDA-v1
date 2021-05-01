"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint

MESSAGE_WRAPPER_NULL = b"\x00" * 30

class MessageWrapper(BigEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("idd_version",             c_char*10),
        ("msg_instance_id",         c_uint32),
        ("message_type",            c_uint32),
        ("message_length",          c_uint32),
        ("stream_id",               c_uint32),
        ("message_properties",      c_uint32)
      ]
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)