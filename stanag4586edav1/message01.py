"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint

MSG01_NULL = b"\x00"*35

class Message01(BigEndianStructure):
    _pack_ = 1
    _fields_ = [
        ("time_stamp",              c_double),
        ("vehicle_id",              c_int32),
        ("cucs_id",                 c_int32),
        ("vsm_id",                  c_int32),
        ("data_link_id",            c_int32),
        ("vehicle_type",            c_ushort),
        ("vehicle_sub_type",        c_ushort),
        ("requested_handover_loi",  c_ubyte),
        ("controlled_station",      c_uint32),
        ("controlled_station_mode", c_ubyte),
        ("wait_for_vehicle_data_link_transition_coordination_message",      c_ubyte),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)