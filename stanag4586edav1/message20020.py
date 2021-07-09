"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

class Message20020(BigEndianStructure, MessageBase):
    """Custom Message 20020 for query response"""
    
    MSGLEN  = 421
    MSGNULL = b"\x00" * MSGLEN

    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("station_number",                      c_uint32),
        ("requested_query_type",                c_byte),
        ("response",                            c_char*400),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        self.has_station_number_field = True

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)

    def get_response(self):
        return self.get_string_field("response")

    def set_response(self, val):
        return self.set_string_field("response", 400, "{:<400}".format(val))
