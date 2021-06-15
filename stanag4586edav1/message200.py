"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

MSG200_NULL = b"\x00"*68

#Constants for set zoom field
MSG200_SET_ZOOM_USE_HV_FOV = 0
MSG200_SET_ZOOM_STOP_ZOOM = 1
MSG200_SET_ZOOM_ZOOM_IN = 2
MSG200_SET_ZOOM_ZOOM_OUT = 3

#Constants for Altitude type field
MSG200_ALTITUDE_TYPE_PRESSURE = 0
MSG200_ALTITUDE_TYPE_BARO = 1
MSG200_ALTITUDE_TYPE_AGL = 2
MSG200_ALTITUDE_TYPE_WSG84 = 3

#Constants for set focus field
MSG200_SET_FOCUS_NO_CHANGE = 0
MSG200_SET_FOCUS_FOCUS_CLOSER = 1
MSG200_SET_FOCUS_FOCUS_FARTHER = 2

#Constants for focus type field
MSG200_FOCUS_TYPE_AUTO = 0
MSG200_FOCUS_TYPE_MANUAL = 1

class Message200(BigEndianStructure, MessageBase):
    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("station_number",                      c_uint32),
        ("set_centreline_azimuth_angle",        c_float),
        ("set_centreline_elevation_angle",      c_float),
        ("set_zoom",                            c_ubyte),
        ("set_horizontal_fov",                  c_float),
        ("set_vertical_fov",                    c_float),
        ("horizontal_slew_rate",                c_float),
        ("vertical_slew_rate",                  c_float),
        ("latitude",                            c_double),
        ("longitude",                           c_double),
        ("altitude",                            c_float),
        ("altitude_type",                       c_ubyte),
        ("set_focus",                           c_ubyte),
        ("focus_type",                          c_ubyte),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)