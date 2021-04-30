"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message300 import *


PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x00" \
b"\x00\x00\x00\x08" \
b"\x00\x00\x00\x08" \
b"\x01" \
b"\x01" \
b"\x01" \

def test_decode_message300():
    msg300 = Message300(PACKET_TO_DECODE)
    
    assert msg300.time_stamp == 0x00
    assert msg300.vehicle_id == 0x50
    assert msg300.cucs_id == 0xA0
    assert msg300.vsm_id == 0x00
    assert msg300.payload_stations_available == 0x08
    assert msg300.station_number == 0x08
    assert msg300.payload_type == 0x01
    assert msg300.station_door == 0x01
    assert msg300.number_of_payload_recording_devices == 0x01

def test_encode_message300():
    msg300 = Message300(MSG300_NULL)

    msg300.time_stamp = 0x00
    msg300.vehicle_id = 0x50
    msg300.cucs_id = 0xA0
    msg300.vsm_id = 0x00
    msg300.payload_stations_available = 0x08
    msg300.station_number = 0x08
    msg300.payload_type = 0x01
    msg300.station_door = 0x01
    msg300.number_of_payload_recording_devices = 0x01

    assert msg300.encode() == PACKET_TO_DECODE