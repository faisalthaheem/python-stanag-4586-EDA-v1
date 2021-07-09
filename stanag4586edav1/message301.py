"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

class Message301(BigEndianStructure, MessageBase):
    MSGLEN  = 63
    MSGNULL = b"\x00" * MSGLEN

    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("vsm_id",                              c_int32),
        ("station_number",                      c_uint32),
        ("eo_ir_type",                          c_char*14),
        ("eo_ir_type_revision_level",           c_ubyte),
        ("eo_vertical_image_dimension",         c_int16),
        ("eo_horizontal_image_dimension",       c_int16),
        ("ir_vertical_image_dimension",         c_int16),
        ("ir_horizontal_image_dimension",       c_int16),
        ("field_of_regard_elevation_min",       c_float),
        ("field_of_regard_elevation_max",       c_float),
        ("field_of_regard_azimuth_min",         c_float),
        ("field_of_regard_azimuth_max",         c_float),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        self.has_station_number_field = True

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)

    def get_eo_ir_type(self):
        return self.get_string_field("eo_ir_type")

    def set_eo_ir_type(self, val):
        return self.set_string_field("eo_ir_type", 14, val)