"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message20040 import *

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x01" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x0B"


def test_decode_message20040():
    msg20040 = Message20040(PACKET_TO_DECODE)

    assert msg20040.time_stamp == 0x00
    assert msg20040.vehicle_id == 0x50
    assert msg20040.cucs_id == 0xA0
    assert msg20040.station_number == 0x01
    assert msg20040.min_height == 1.0
    assert msg20040.max_height == 1.0
    assert msg20040.current_height == 1.0
    assert msg20040.error_code == 11

def test_encode_message20040():
    msg20040 = Message20040(Message20040.MSGNULL)
    
    msg20040.time_stamp = 0x00
    msg20040.vehicle_id = 0x50
    msg20040.cucs_id = 0xA0
    msg20040.station_number = 0x01
    msg20040.command_type = 0x0A
    msg20040.min_height = 1.0
    msg20040.max_height = 1.0
    msg20040.current_height = 1.0
    msg20040.error_code = 11

    assert msg20040.encode() == PACKET_TO_DECODE