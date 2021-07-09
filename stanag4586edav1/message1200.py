"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

class Message1200(BigEndianStructure, MessageBase):
    MSGLEN  = 35
    MSGNULL = b"\x00" * MSGLEN

    _pack_ = 1
    _fields_ = [
        ("time_stamp",              c_double),
        ("vehicle_id",              c_int32),
        ("cucs_id",                 c_int32),
        ("vsm_id",                  c_int32),
        ("data_link_id",            c_int32),
        ("request_type",            c_ubyte),
        ("requested_message",       c_uint32),
        ("requested_field",         c_ubyte),
        ("station_number",          c_uint32),
        ("sensor_select",           c_ubyte),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        self.has_station_number_field = True

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)