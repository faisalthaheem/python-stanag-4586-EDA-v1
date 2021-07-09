"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase


class Message20010(BigEndianStructure, MessageBase):
    """Custom Message 20010 for querying stations"""
    
    MSGLEN  = 21
    MSGNULL = b"\x00" * MSGLEN

    QUERY_TYPE_SEND_STATION_TYPE = 10
    QUERY_TYPE_SEND_CONFIG = 20

    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("station_number",                      c_uint32),
        ("query_type",                          c_byte)
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        self.has_station_number_field = True

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)