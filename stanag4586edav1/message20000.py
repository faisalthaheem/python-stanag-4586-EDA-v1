"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

MSG20000_NULL = b"\x00"*68

MSG20000_PAN_DIRECTION_LEFT = -1
MSG20000_PAN_DIRECTION_NONE = 0
MSG20000_PAN_DIRECTION_RIGHT = 1

MSG20000_TILT_DIRECTION_UP = 1
MSG20000_TILT_DIRECTION_NONE = 0
MSG20000_TILT_DIRECTION_DOWN = -1

class Message20000(BigEndianStructure, MessageBase):
    """Custom Message 20000 for continually Panning and Tilting EO payloads"""
    
    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("pan_force",                           c_float),
        ("pan_direction",                       c_byte),
        ("tilt_force",                          c_float),
        ("tilt_direction",                      c_byte),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)