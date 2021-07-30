"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from .message_base import MessageBase


class Message20030(MessageBase):
    """Custom Message 20030 for mast comamnds"""
    
    MSGLEN  = 25
    MSGNULL = b"\x00" * MSGLEN

    CMD_TYPE_MOVE_UP = 10
    CMD_TYPE_MOVE_DOWN = 20
    CMD_TYPE_MOVE_ABSOLUTE = 30

    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("station_number",                      c_uint32),
        ("command_type",                        c_ubyte),
        ("absolute_height",                     c_float),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def getStationId(self):
       return self.station_number