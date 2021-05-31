"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

MSG300_NULL = b"\x00"*31
STATION_TYPE_UNSPECIFIED = 0x00
STATION_TYPE_EO = 0x01
STATION_TYPE_IR = 0x02
STATION_TYPE_EOIR = 0x03
STATION_TYPE_SAR = 0x04
STATION_TYPE_FIXED_CAMERA = 0x05
STATION_TYPE_COMMS_RELAY = 0x06
STATION_TYPE_DISPENSABLE_PAYLOAD = 0x07
STATION_TYPE_RECORDER = 0x08
STATION_TYPE_PAYLOAD_BAY_DOOR = 0x09
STATION_TYPE_CBRN = 0x0A
STATION_TYPE_SMS = 0x0B

class Message300(BigEndianStructure, MessageBase):
    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("vsm_id",                              c_int32),
        ("payload_stations_available",          c_uint32),
        ("station_number",                      c_uint32),
        ("payload_type",                        c_ubyte),
        ("station_door",                        c_ubyte),
        ("number_of_payload_recording_devices", c_ubyte),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)