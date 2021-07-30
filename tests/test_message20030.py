"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message20030 import *

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x01" \
b"\x0A" \
b"\x3f\x80\x00\x00" 


def test_decode_message20030():
    msg20030 = Message20030(PACKET_TO_DECODE)

    assert msg20030.time_stamp == 0x00
    assert msg20030.vehicle_id == 0x50
    assert msg20030.cucs_id == 0xA0
    assert msg20030.station_number == 0x01
    assert msg20030.command_type == 10
    assert msg20030.absolute_height == 1.0

def test_encode_message20030():
    msg20030 = Message20030(Message20030.MSGNULL)
    
    msg20030.time_stamp = 0x00
    msg20030.vehicle_id = 0x50
    msg20030.cucs_id = 0xA0
    msg20030.station_number = 0x01
    msg20030.command_type = 0x0A
    msg20030.absolute_height = 1.0

    assert msg20030.encode() == PACKET_TO_DECODE