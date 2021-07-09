"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message200 import *
import pytest

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x01" \
b"\x42\x04\x00\x00" \
b"\x42\x04\x00\x00" \
b"\x03" \
b"\x42\x04\x00\x00" \
b"\x42\x04\x00\x00" \
b"\x42\x04\x00\x00" \
b"\x42\x04\x00\x00" \
b"\x40\x39\x00\x00\x00\x00\x00\x00" \
b"\x40\x39\x00\x00\x00\x00\x00\x00" \
b"\x42\x04\x00\x00" \
b"\x02" \
b"\x01" \
b"\x01" \

def test_decode_message200():
    msg200 = Message200(PACKET_TO_DECODE)

    assert msg200.time_stamp == 0x00
    assert msg200.vehicle_id == 0x50
    assert msg200.cucs_id == 0xA0
    assert msg200.station_number == 0x01
    assert msg200.set_centreline_azimuth_angle == pytest.approx(33.0)
    assert msg200.set_centreline_elevation_angle == pytest.approx(33.0)
    assert msg200.set_zoom == 0x03
    assert msg200.set_horizontal_fov == pytest.approx(33.0)
    assert msg200.set_vertical_fov == pytest.approx(33.0)
    assert msg200.horizontal_slew_rate == pytest.approx(33.0)
    assert msg200.vertical_slew_rate == pytest.approx(33.0)
    assert msg200.latitude == pytest.approx(25.0)
    assert msg200.longitude == pytest.approx(25.0)
    assert msg200.altitude == pytest.approx(33.0)
    assert msg200.altitude_type == 2
    assert msg200.set_focus == 1
    assert msg200.focus_type == 1

def test_encode_message200():
    msg200 = Message200(Message200.MSGNULL)

    msg200.time_stamp = 0x00
    msg200.vehicle_id = 0x50
    msg200.cucs_id = 0xA0
    msg200.station_number = 0x01
    msg200.set_centreline_azimuth_angle = 33.0
    msg200.set_centreline_elevation_angle = 33.0
    msg200.set_zoom = Message200.SET_ZOOM_ZOOM_OUT
    msg200.set_horizontal_fov = 33.0
    msg200.set_vertical_fov = 33.0
    msg200.horizontal_slew_rate = 33.0
    msg200.vertical_slew_rate = 33.0
    msg200.latitude = 25.0
    msg200.longitude = 25.0
    msg200.altitude = 33.0
    msg200.altitude_type = Message200.ALTITUDE_TYPE_AGL
    msg200.set_focus = 1
    msg200.focus_type = Message200.FOCUS_TYPE_MANUAL

    assert msg200.encode() == PACKET_TO_DECODE