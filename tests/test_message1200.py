"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message1200 import *


PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x00" \
b"\x00\x00\x00\x11" \
b"\x02" \
b"\x00\x00\x00\x33" \
b"\x01" \
b"\x00\x00\x00\x40" \
b"\x03"


def test_decode_message1200():
    msg1200 = Message1200(PACKET_TO_DECODE)
    
    assert msg1200.time_stamp == 0x00
    assert msg1200.vehicle_id == 0x50
    assert msg1200.cucs_id == 0xA0
    assert msg1200.vsm_id == 0x00
    assert msg1200.data_link_id == 0x11
    assert msg1200.request_type == 0x02
    assert msg1200.requested_message == 0x33
    assert msg1200.requested_field == 0x01
    assert msg1200.station_number == 0x40
    assert msg1200.sensor_select == 0x03

def test_encode_message01():
    msg1200 = Message1200(MSG1200_NULL)

    msg1200.time_stamp = 0x00
    msg1200.vehicle_id = 0x50
    msg1200.cucs_id = 0xA0
    msg1200.vsm_id = 0x00
    msg1200.data_link_id = 0x11
    msg1200.request_type = 0x02
    msg1200.requested_message = 0x33
    msg1200.requested_field = 0x01
    msg1200.station_number = 0x40
    msg1200.sensor_select = 0x03

    assert msg1200.encode() == PACKET_TO_DECODE