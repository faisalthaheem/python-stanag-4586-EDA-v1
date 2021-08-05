"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from .message_base import MessageBase

class Message201(MessageBase):
    """EO/IR/Laser Payload Command - This message shall be used to command EO/IR/Laser payloads with the exception of
payload pointing commands"""
    MSGLEN  = 33
    MSGNULL = b"\x00" * MSGLEN

    ADDRESSED_SENSOR_EO = 0X01
    ADDRESSED_SENSOR_IR = 0X02
    ADDRESSED_SENSOR_PLSPECIFIC = 0X04

    SYSTEM_OPERATING_MODE_STOW = 0
    SYSTEM_OPERATING_MODE_OFF = 1
    SYSTEM_OPERATING_MODE_CAGE = 2
    SYSTEM_OPERATING_MODE_INIT = 3
    SYSTEM_OPERATING_MODE_STANDBY = 4
    SYSTEM_OPERATING_MODE_ACTIVE = 5
    SYSTEM_OPERATING_MODE_CALIBRATE = 6
    SYSTEM_OPERATING_MODE_RESERVED = 7
    SYSTEM_OPERATING_MODE_PLSPECIFIC = 10

    EO_SENSOR_MODE_BW = 0
    EO_SENSOR_MODE_COLOR = 1

    IR_POLARITY_BLACK_HOT = 0
    IR_POLARITY_WHITE_HOT = 1

    IMAGE_OUTPUT_NONE = 0
    IMAGE_OUTPUT_EO = 1
    IMAGE_OUTPUT_IR = 2
    IMAGE_OUTPUT_BOTH = 3
    IMAGE_OUTPUT_PLSPECIFIC = 4


    EO_IR_POINTING_MODE_NO_VALUE = 0
    EO_IR_POINTING_MODE_ANGLE_RELATIVE_TO_UA = 1
    EO_IR_POINTING_MODE_SLEWING_RATE_RELATIVE_TO_UA = 2
    EO_IR_POINTING_MODE_SLEWING_RATE_RELATIVE_INERTIAL = 3
    EO_IR_POINTING_MODE_LAT_LONG_SLAVED = 4
    EO_IR_POINTING_MODE_TARGET_SLAVED = 5
    EO_IR_POINTING_MODE_RESERVED = 6
    EO_IR_POINTING_MODE_PLSPECIFIC = 10

    LASER_POINTER_OFF = 0
    LASER_POINTER_ARM = 51
    LASER_POINTER_ON_SAFE = 68
    LASER_POINTER_FIRE = 238

    LRF_OFF = 0
    LRF_ARM = 51
    LRF_ON_SAFE = 68
    LRF_FIRE_ONE_PULSE = 85
    LRF_FIRE_MULTIPLE_PULSES = 238

    SELECT_LRF_PULSE_FIRST = 1
    SELECT_LRF_PULSE_LAST = 2

    INIT_LASER_DESIGNATOR_OFF = 0
    INIT_LASER_DESIGNATOR_ARM = 51
    INIT_LASER_DESIGNATOR_ON_SAFE = 68
    INIT_LASER_DESIGNATOR_FIRE = 85

    PREPLAN_MODE_OPERATE_IN_PREPLAN = 0
    PREPLAN_MODE_OPERATE_IN_MANUAL = 1
    
    _pack_ = 1
    _fields_ = [
        ("time_stamp",                          c_double),
        ("vehicle_id",                          c_int32),
        ("cucs_id",                             c_int32),
        ("station_number",                      c_uint32),
        ("addressed_sensor",                    c_ubyte),
        ("system_operating_mode",               c_ubyte),
        ("set_eo_sensor_mode",                  c_ubyte),
        ("set_ir_polarity",                     c_ubyte),
        ("image_output",                        c_ubyte),
        ("set_eo_ir_pointing_mode",             c_ubyte),
        ("fire_laser_pointer",                  c_ubyte),
        ("fire_laser_rangefinder",              c_ubyte),
        ("select_lrf_first_last_pulse",         c_ubyte),
        ("set_laser_designator_code",           c_ushort),
        ("initiate_laser_designator",           c_ubyte),
        ("preplan_mode",                        c_ubyte),
      ]
    
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def getStationId(self):
       return self.station_number