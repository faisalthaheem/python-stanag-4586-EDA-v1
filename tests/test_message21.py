"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message21 import *


PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x00" \
b"\x00\x00\x00\x11" \
b"\x08" \
b"\x00" \
b"\x00\x00\x00\x00" \
b"\x00" \
b"\x00\x01" \
b"\x31\x32" 

def test_decode_message21():
    msg21 = Message21(PACKET_TO_DECODE)
    
    assert msg21.time_stamp == 0x00
    assert msg21.vehicle_id == 0x50
    assert msg21.cucs_id == 0xA0
    assert msg21.vsm_id == 0x00
    assert msg21.data_link_id == 0x11
    assert msg21.loi_authorized == 0x08
    assert msg21.loi_granted == 0x00
    assert msg21.controlled_station == 0x00
    assert msg21.controlled_station_mode == 0x00
    assert msg21.vehicle_type == 0x01
    assert msg21.vehicle_sub_type == 0x3132

def test_encode_message01():
    msg21 = Message21(Message21.MSGNULL)

    msg21.time_stamp = 0x00
    msg21.vehicle_id = 0x50
    msg21.cucs_id = 0xA0
    msg21.vsm_id = 0x00
    msg21.data_link_id = 0x11
    msg21.loi_authorized = 0x08
    msg21.loi_granted = 0x00
    msg21.controlled_station = 0x00
    msg21.controlled_station_mode = 0x00
    msg21.vehicle_type = 0x01
    msg21.vehicle_sub_type = 0x3132

    assert msg21.encode() == PACKET_TO_DECODE