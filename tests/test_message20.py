"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message20 import *

#line 1, vehicle_id = 0x50, cucs_id = 0xA0, upto vsm id
#line 2, vehicle type is 39 rq-14a dragon eye, requested loi = 1, controlled station mode = 1

PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x00" \
b"\x00\x00\x00\x11" \
b"\x00\x39" \
b"\x00\x00" \
b"\xFA" \
b"\x31\x32\x33\x34" \
b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x31\x32\x33\x34" \
b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x31\x32\x33\x34" \
b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\xAB\xCD"

def test_decode_message20():
    msg20 = Message20(PACKET_TO_DECODE)
    
    assert msg20.time_stamp == 0x00
    assert msg20.vehicle_id == 0x50
    assert msg20.cucs_id == 0xA0
    assert msg20.vsm_id == 0x00
    assert msg20.vehicle_id_update == 0x11
    assert msg20.vehicle_type == 0x39
    assert msg20.vehicle_sub_type == 00
    assert msg20.owning_id == 0xFA
    assert msg20.tail_number == b"\x31\x32\x33\x34"
    assert msg20.mission_id == b"\x31\x32\x33\x34"
    assert msg20.atc_call_sign == b"\x31\x32\x33\x34"
    assert msg20.configuration_checksum == 0xABCD

def test_encode_message20():
    msg20 = Message20(Message20.MSGNULL)

    msg20.time_stamp = 0x00
    msg20.vehicle_id = 0x50
    msg20.cucs_id = 0xA0
    msg20.vsm_id = 0x00
    msg20.vehicle_id_update = 0x11
    msg20.vehicle_type = 0x39
    msg20.vehicle_sub_type = 00
    msg20.owning_id = 0xFA
    msg20.tail_number = b"\x31\x32\x33\x34"
    msg20.mission_id = b"\x31\x32\x33\x34"
    msg20.atc_call_sign = b"\x31\x32\x33\x34"
    msg20.configuration_checksum = 0xABCD

    assert msg20.encode() == PACKET_TO_DECODE


####
#### Tail number
def test_encode_decode_tail_number():
    msg20 = Message20(Message20.MSGNULL)

    msg20.set_tail_number('99876')
    assert '99876' == msg20.get_tail_number()

def test_encode_tail_number_exceeding_field_length():
    msg20 = Message20(Message20.MSGNULL)

    assert False == msg20.set_tail_number('12345678901234567')
    
def test_encode_tail_number_0_field_length():
    msg20 = Message20(Message20.MSGNULL)

    assert False == msg20.set_tail_number('')
    
####
#### Mission id
def test_encode_decode_mission_id():
    msg20 = Message20(Message20.MSGNULL)

    mission_id = 'ALPHA FOXTROT'
    msg20.set_mission_id(mission_id)
    assert mission_id == msg20.get_mission_id()

def test_encode_mission_id_exceeding_field_length():
    msg20 = Message20(Message20.MSGNULL)

    assert False == msg20.set_mission_id('123456789012345678901')
    
def test_encode_mission_id_0_field_length():
    msg20 = Message20(Message20.MSGNULL)

    assert False == msg20.set_mission_id('')

####
#### ATC call sign
def test_encode_decode_mission_id():
    msg20 = Message20(Message20.MSGNULL)

    atc_call_sign = 'CHARLIE TANGO'
    msg20.set_atc_call_sign(atc_call_sign)
    assert atc_call_sign == msg20.get_atc_call_sign()

def test_encode_mission_id_exceeding_field_length():
    msg20 = Message20(Message20.MSGNULL)

    assert False == msg20.set_atc_call_sign('123456789012345678901234567890123')
    
def test_encode_mission_id_0_field_length():
    msg20 = Message20(Message20.MSGNULL)

    assert False == msg20.set_atc_call_sign('')