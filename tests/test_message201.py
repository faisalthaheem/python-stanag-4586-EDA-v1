"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message201 import *
import pytest

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x01" \
b"\x04" \
b"\x05" \
b"\x01" \
b"\x01" \
b"\x03" \
b"\x05" \
b"\xEE" \
b"\xEE" \
b"\x02" \
b"\x00\x01" \
b"\x55" \
b"\x01"


def test_decode_message201():
    msg201 = Message201(PACKET_TO_DECODE)

    assert msg201.time_stamp == 0x00
    assert msg201.vehicle_id == 0x50
    assert msg201.cucs_id == 0xA0
    assert msg201.station_number == 0x01
    assert msg201.addressed_sensor == Message201.ADDRESSED_SENSOR_PLSPECIFIC
    assert msg201.system_operating_mode == Message201.SYSTEM_OPERATING_MODE_ACTIVE
    assert msg201.set_eo_sensor_mode == Message201.EO_SENSOR_MODE_COLOR
    assert msg201.set_ir_polarity == Message201.IR_POLARITY_WHITE_HOT
    assert msg201.image_output == Message201.IMAGE_OUTPUT_BOTH
    assert msg201.set_eo_ir_pointing_mode == Message201.EO_IR_POINTING_MODE_TARGET_SLAVED
    assert msg201.fire_laser_pointer == Message201.LASER_POINTER_FIRE
    assert msg201.fire_laser_rangefinder == Message201.LRF_FIRE_MULTIPLE_PULSES
    assert msg201.select_lrf_first_last_pulse == Message201.SELECT_LRF_PULSE_LAST
    assert msg201.set_laser_designator_code == 1
    assert msg201.initiate_laser_designator == Message201.INIT_LASER_DESIGNATOR_FIRE
    assert msg201.preplan_mode == Message201.PREPLAN_MODE_OPERATE_IN_MANUAL

def test_encode_message201():
    msg201 = Message201(Message201.MSGNULL)

    msg201.time_stamp = 0x00
    msg201.vehicle_id = 0x50
    msg201.cucs_id = 0xA0
    msg201.station_number = 0x01
    msg201.addressed_sensor = Message201.ADDRESSED_SENSOR_PLSPECIFIC
    msg201.system_operating_mode = Message201.SYSTEM_OPERATING_MODE_ACTIVE
    msg201.set_eo_sensor_mode = Message201.EO_SENSOR_MODE_COLOR
    msg201.set_ir_polarity = Message201.IR_POLARITY_WHITE_HOT
    msg201.image_output = Message201.IMAGE_OUTPUT_BOTH
    msg201.set_eo_ir_pointing_mode = Message201.EO_IR_POINTING_MODE_TARGET_SLAVED
    msg201.fire_laser_pointer = Message201.LASER_POINTER_FIRE
    msg201.fire_laser_rangefinder = Message201.LRF_FIRE_MULTIPLE_PULSES
    msg201.select_lrf_first_last_pulse = Message201.SELECT_LRF_PULSE_LAST
    msg201.set_laser_designator_code = 1
    msg201.initiate_laser_designator = Message201.INIT_LASER_DESIGNATOR_FIRE
    msg201.preplan_mode = Message201.PREPLAN_MODE_OPERATE_IN_MANUAL

    assert msg201.encode() == PACKET_TO_DECODE