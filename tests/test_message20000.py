"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message20000 import *
import pytest

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x01" \
b"\x42\x04\x00\x00" \
b"\x01" \
b"\x42\x04\x00\x00" \
b"\xFF" \

def test_decode_message20000():
    msg20000 = Message20000(PACKET_TO_DECODE)

    assert msg20000.time_stamp == 0x00
    assert msg20000.vehicle_id == 0x50
    assert msg20000.cucs_id == 0xA0
    assert msg20000.station_number == 0x01
    assert msg20000.pan_force == pytest.approx(33.0)
    assert msg20000.pan_direction == MSG20000_PAN_DIRECTION_RIGHT
    assert msg20000.tilt_force == pytest.approx(33.0)
    assert msg20000.tilt_direction == MSG20000_TILT_DIRECTION_DOWN

def test_encode_message200():
    msg20000 = Message20000(MSG20000_NULL)
    
    msg20000.time_stamp = 0x00
    msg20000.vehicle_id = 0x50
    msg20000.cucs_id = 0xA0
    msg20000.station_number = 0x01
    msg20000.pan_force = 33.0
    msg20000.pan_direction = MSG20000_PAN_DIRECTION_RIGHT
    msg20000.tilt_force = 33.0
    msg20000.tilt_direction = MSG20000_TILT_DIRECTION_DOWN

    assert msg20000.encode() == PACKET_TO_DECODE