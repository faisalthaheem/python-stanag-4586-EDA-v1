"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

class Message20(BigEndianStructure, MessageBase):
    MSGLEN  = 99
    MSGNULL = b"\x00" * MSGLEN

    _pack_ = 1
    _fields_ = [
        ("time_stamp",              c_double),
        ("vehicle_id",              c_int32),
        ("cucs_id",                 c_int32),
        ("vsm_id",                  c_int32),
        ("vehicle_id_update",       c_int32),
        ("vehicle_type",            c_ushort),
        ("vehicle_sub_type",        c_ushort),
        ("owning_id",               c_ubyte),
        ("tail_number",             c_char*16),
        ("mission_id",              c_char*20),
        ("atc_call_sign",           c_char*32),
        ("configuration_checksum",  c_ushort),
      ]

    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)

    def get_tail_number(self):
        return self.get_string_field("tail_number")

    def set_tail_number(self, val):
        return self.set_string_field("tail_number", 16, val)

    def get_mission_id(self):
        return self.get_string_field("mission_id")

    def set_mission_id(self, val):
        return self.set_string_field("mission_id", 20, val)

    def get_atc_call_sign(self):
        return self.get_string_field("atc_call_sign")

    def set_atc_call_sign(self, val):
        return self.set_string_field("atc_call_sign", 32, val)