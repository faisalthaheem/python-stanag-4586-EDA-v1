"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

class Message21(BigEndianStructure, MessageBase):
    MSGLEN  = 35
    MSGNULL = b"\x00" * MSGLEN

    CONTROLLED_STATION_MODE_NOT_IN_CONTROL = 0
    CONTROLLED_STATION_MODE_IN_CONTROL = 1

    VEHICLE_TYPE_UAV = 10000
    VEHICLE_TYPE_UGV = 11000
    VEHICLE_TYPE_USV = 12000
    VEHICLE_TYPE_UUV = 13000

    UGV_SUB_TYPE_MULE       = 1000 #LOAD CARRYING
    UGV_SUB_TYPE_SURV       = 1010 #SURVEILLANCE
    UGV_SUB_TYPE_SENTRY     = 1020 #WITH A GUN AND EO
    UGV_SUB_TYPE_SAM        = 1030 #SURFACE TO AIR MISSLE CARRYING

    _pack_ = 1
    _fields_ = [
        ("time_stamp",              c_double),
        ("vehicle_id",              c_int32),
        ("cucs_id",                 c_int32),
        ("vsm_id",                  c_int32),
        ("data_link_id",            c_int32),
        ("loi_authorized",          c_ubyte),
        ("loi_granted",             c_ubyte),
        ("controlled_station",      c_uint32),
        ("controlled_station_mode", c_ubyte),
        ("vehicle_type",            c_ushort),
        ("vehicle_sub_type",        c_ushort),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)

    def vehicle_type_to_str(self, vehicle_type):

        str_type = "unknown"

        if vehicle_type == self.VEHICLE_TYPE_UAV:
            str_type = "UAV"
        elif vehicle_type == self.VEHICLE_TYPE_UGV:
            str_type = "UGV"
        elif vehicle_type == self.VEHICLE_TYPE_USV:
            str_type = "USV"
        elif vehicle_type == self.VEHICLE_TYPE_UUV:
            str_type = "UUV"

        return str_type

    def vehicle_sub_type_to_str(self, vehicle_sub_type):

        str_type = "unknown"

        if vehicle_sub_type == self.UGV_SUB_TYPE_MULE:
            str_type = "MULE"
        elif vehicle_sub_type == self.UGV_SUB_TYPE_SURV:
            str_type = "SURVEILLANCE"
        elif vehicle_sub_type == self.UGV_SUB_TYPE_SENTRY:
            str_type = "SENTRY"
        elif vehicle_sub_type == self.UGV_SUB_TYPE_SAM:
            str_type = "SAM"

        return str_type