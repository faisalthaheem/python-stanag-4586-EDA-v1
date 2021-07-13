"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

class Message300(BigEndianStructure, MessageBase):
    
    MSGLEN  = 31
    MSGNULL = b"\x00" * MSGLEN

    PAYLOAD_TYPE_UNSPECIFIED = 0x00
    PAYLOAD_TYPE_EO = 0x01
    PAYLOAD_TYPE_IR = 0x02
    PAYLOAD_TYPE_EOIR = 0x03
    PAYLOAD_TYPE_SAR = 0x04
    PAYLOAD_TYPE_FIXED_CAMERA = 0x05
    PAYLOAD_TYPE_COMMS_RELAY = 0x06
    PAYLOAD_TYPE_DISPENSABLE_PAYLOAD = 0x07
    PAYLOAD_TYPE_RECORDER = 0x08
    PAYLOAD_TYPE_PAYLOAD_BAY_DOOR = 0x09
    PAYLOAD_TYPE_CBRN = 0x0A
    PAYLOAD_TYPE_SMS = 0x0B
    
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
        self.has_station_number_field = True

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)

    def payload_type_to_str(self, pl_type):
        str_type = "unspecified"

        if pl_type == self.PAYLOAD_TYPE_EO:
            str_type = "EO"
        elif pl_type == self.PAYLOAD_TYPE_IR:
            str_type = "IR"
        elif pl_type == self.PAYLOAD_TYPE_EOIR:
            str_type = "EO/IR"
        elif pl_type == self.PAYLOAD_TYPE_SAR:
            str_type = "SAR"
        elif pl_type == self.PAYLOAD_TYPE_FIXED_CAMERA:
            str_type = "FIXED CAMERA"
        elif pl_type == self.PAYLOAD_TYPE_COMMS_RELAY:
            str_type = "COMMS RELAY"
        elif pl_type == self.PAYLOAD_TYPE_DISPENSABLE_PAYLOAD:
            str_type = "DISPENSABLE PAYLOAD"
        elif pl_type == self.PAYLOAD_TYPE_RECORDER:
            str_type = "RECORDER"
        elif pl_type == self.PAYLOAD_TYPE_PAYLOAD_BAY_DOOR:
            str_type = "PAYLOAD BAY DOOR"
        elif pl_type == self.PAYLOAD_TYPE_CBRN:
            str_type = "CBRN"
        elif pl_type == self.PAYLOAD_TYPE_SMS:
            str_type = "SMS"                    
        
        return str_type