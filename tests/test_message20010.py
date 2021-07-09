"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message20010 import *

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x01" \
b"\x14"

def test_decode_message20010():
    msg20010 = Message20010(PACKET_TO_DECODE)

    assert msg20010.time_stamp == 0x00
    assert msg20010.vehicle_id == 0x50
    assert msg20010.cucs_id == 0xA0
    assert msg20010.station_number == 0x01
    assert msg20010.query_type == Message20010.QUERY_TYPE_SEND_CONFIG

def test_encode_message20010():
    msg20010 = Message20010(Message20010.MSGNULL)
    
    msg20010.time_stamp = 0x00
    msg20010.vehicle_id = 0x50
    msg20010.cucs_id = 0xA0
    msg20010.station_number = 0x01
    msg20010.query_type = Message20010.QUERY_TYPE_SEND_CONFIG

    assert msg20010.encode() == PACKET_TO_DECODE