"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint

class Message01(BigEndianStructure):
    MSGLEN  = 35
    MSGNULL = b"\x00" * MSGLEN

    BROADCAST_ID = 0xFFFFFFFF
    LOI_02 = 0x01 #Monitoring the UA / PL
    LOI_03 = 0x02 #Controlling the PL
    LOI_04 = 0x04 #Controlling the UA without takeoff/landing
    LOI_05 = 0x08 #Controlling the UA with takeoff/landing

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

    def make_discovery_message(self, cucs_id):
        self.vehicle_id = self.BROADCAST_ID
        self.cucs_id = cucs_id
        self.vsm_id = self.BROADCAST_ID
        self.data_link_id = 0
        self.vehicle_type = 0
        self.vehicle_sub_type = 0
        self.requested_handover_loi = 0
        self.controlled_station = self.BROADCAST_ID
        self.controlled_station_mode = 0
        self.wait_for_vehicle_data_link_transition_coordination_message = 0