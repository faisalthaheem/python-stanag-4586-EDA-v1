"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint
from .message_base import MessageBase

class Message302(BigEndianStructure, MessageBase):
    MSGLEN  = 82
    MSGNULL = b"\x00" * MSGLEN

    _pack_ = 1
    _fields_ = [
        ("time_stamp",                                  c_double),
        ("vehicle_id",                                  c_int32),
        ("cucs_id",                                     c_int32),
        ("vsm_id",                                      c_int32),
        ("station_number",                              c_uint32),
        ("addressed_sensor",                            c_ubyte),
        ("system_operating_mode_state",                 c_ubyte),
        ("eo_sensor_mode_status",                       c_ubyte),
        ("ir_polarity_status",                          c_ubyte),
        ("image_output_state",                          c_ubyte),
        ("actual_centerline_elevation_angle",           c_float),
        ("actual_vertical_field_of_view",               c_float),
        ("actual_centerline_azimuth_angle",             c_float),
        ("actual_horizontal_field_of_view",             c_float),
        ("actual_sensor_rotation_angle",                c_float),
        ("image_position",                              c_ubyte),
        ("latitude",                                    c_double),
        ("longitude",                                   c_double),
        ("altitude",                                    c_float),
        ("pointing_mode_state",                         c_ubyte),
        ("preplan_mode",                                c_ubyte),
        ("reported_range",                              c_float),
        ("fire_laser_pointer_status",                   c_ubyte),
        ("fire_laser_rangefinder_status",               c_ubyte),
        ("selected_laser_rangefinder_first_last_pulse", c_ubyte),
        ("laser_designator_code",                       c_ushort),
        ("laser_designator_status",                     c_ubyte),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        self.has_station_number_field = True

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)


class Message302_addressed_sensor:
    EO = 0x01
    IR = 0x02
    PAYLOAD_SPECIFIC = 0x04

class Message302_system_operating_mode_state:
    STOWED = 0
    OFF = 1
    CAGED = 2
    INITIALISING = 3
    STANDBY = 4
    ACTIVE = 5
    CALIBRATING = 6

class Message302_eo_sensor_mode_status:
    BW_MODE = 0
    COLOR_MODE = 1

class Message302_ir_polarity_status:
    BLACK_HOT = 0
    WHITE_HOT = 1

class Message302_image_output_state:
    NONE = 0
    EO = 1
    IR = 2
    BOTH = 3
    PAYLOAD_SPECIFIC = 4

class Message302_pointing_mode_state:
    NO_VALUE = 0
    ANGLE_RELATIVE_TO_UA = 1
    SLEWING_RATE_RELATIVE_TO_UA = 2
    SLEWING_RATE_RELATIVE_TO_INERTIAL = 3
    LAT_LONG_SLAVED = 4
    TARGET_SLAVED = 5

class Message302_preplan_mode:
    OPERATE_IN_PREPLAN_MODE = 1
    OPERATE_IN_MANUAL_MODE = 2

class Message302_fire_laser_pointer_status:
    OFF = 0
    ON_SAFED = 1
    ARMED = 2
    FIRING = 3
    MASKED = 4

class Message302_fire_laser_rangefinder_status:
    OFF = 0
    ON_SAFED = 1
    ARMED = 2
    RECHARGING = 3
    FIRING = 4
    MASKED = 5

class Message302_selected_laser_rangefinder_first_last_pulse:
    FIRST = 1
    LAST = 2

class Message302_laser_designator_status:
    OFF = 0
    ON  = 1
    ARMED = 2
    FIRING = 3
    MASKED = 4
