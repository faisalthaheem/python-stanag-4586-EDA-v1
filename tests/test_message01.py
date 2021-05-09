"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message01 import *

#line 1, vehicle_id = 0x50, cucs_id = 0xA0, upto vsm id
#line 2, vehicle type is 39 rq-14a dragon eye, requested loi = 1, controlled station mode = 1

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x50\x00\x00\x00\xA0\x00\x00\x00\x00" \
b"\x00\x00\x00\x00\x00\x39\x00\x00\x01\x00\x00\x00\x00\x01\x00"

PACKET_DISCOVERY_MSG = b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xfa\xfa\xfa\xfa\xff\xff\xff' \
b'\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00'

def test_decode_message01():
    msg01 = Message01(PACKET_TO_DECODE)
    
    assert msg01.time_stamp == 0x00
    assert msg01.vehicle_id == 0x50
    assert msg01.cucs_id == 0xA0
    assert msg01.vsm_id == 0x00
    assert msg01.data_link_id == 0x00
    assert msg01.vehicle_type == 0x39
    assert msg01.vehicle_sub_type == 00
    assert msg01.requested_handover_loi == 0x01
    assert msg01.controlled_station == 0x00
    assert msg01.controlled_station_mode == 0x01
    assert msg01.wait_for_vehicle_data_link_transition_coordination_message == 0x00

def test_encode_message01():
    msg01 = Message01(MSG01_NULL)

    msg01.time_stamp = 0x00
    msg01.vehicle_id = 0x50
    msg01.cucs_id = 0xA0
    msg01.vsm_id = 0x00
    msg01.data_link_id = 0x00
    msg01.vehicle_type = 0x39
    msg01.vehicle_sub_type = 00
    msg01.requested_handover_loi = 0x01
    msg01.controlled_station = 0x00
    msg01.controlled_station_mode = 0x01
    msg01.wait_for_vehicle_data_link_transition_coordination_message = 0x00

    assert msg01.encode() == PACKET_TO_DECODE

def test_make_discovery_message():
    msg01 = Message01(MSG01_NULL)
    msg01.make_discovery_message(0xFAFAFAFA)

    assert msg01.encode() == PACKET_DISCOVERY_MSG