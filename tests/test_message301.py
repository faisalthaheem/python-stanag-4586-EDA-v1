"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message301 import *


PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x00" \
b"\x00\x00\x00\x08" \
b"\x31\x31\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x01" \
b"\x03\x00" \
b"\x04\x00" \
b"\x03\x00" \
b"\x04\x00" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" 

def test_decode_message301():
    msg301 = Message301(PACKET_TO_DECODE)
    
    assert msg301.time_stamp == 0x00
    assert msg301.vehicle_id == 0x50
    assert msg301.cucs_id == 0xA0
    assert msg301.vsm_id == 0x00
    assert msg301.station_number == 0x08
    assert msg301.eo_ir_type == b"\x31\x31"
    assert msg301.eo_ir_type_revision_level == 0x01
    assert msg301.eo_vertical_image_dimension == 768
    assert msg301.eo_horizontal_image_dimension == 1024
    assert msg301.ir_vertical_image_dimension == 768
    assert msg301.ir_horizontal_image_dimension == 1024
    assert msg301.field_of_regard_elevation_min == 1.0
    assert msg301.field_of_regard_elevation_max == 1.0
    assert msg301.field_of_regard_azimuth_min == 1.0
    assert msg301.field_of_regard_azimuth_max == 1.0


def test_encode_message301():
    msg301 = Message301(MSG301_NULL)

    msg301.time_stamp = 0x00
    msg301.vehicle_id = 0x50
    msg301.cucs_id = 0xA0
    msg301.vsm_id = 0x00
    msg301.station_number = 0x08
    msg301.eo_ir_type = b"\x31\x31"
    msg301.eo_ir_type_revision_level = 0x01
    msg301.eo_vertical_image_dimension = 768
    msg301.eo_horizontal_image_dimension = 1024
    msg301.ir_vertical_image_dimension = 768
    msg301.ir_horizontal_image_dimension = 1024
    msg301.field_of_regard_elevation_min = 1.0
    msg301.field_of_regard_elevation_max = 1.0
    msg301.field_of_regard_azimuth_min = 1.0
    msg301.field_of_regard_azimuth_max = 1.0

    assert msg301.encode() == PACKET_TO_DECODE

def test_set_get_eo_ir_type():
    msg301 = Message301(MSG301_NULL)

    ID_TO_TEST = "valid id"
    assert msg301.set_eo_ir_type(ID_TO_TEST) == True

    assert msg301.get_eo_ir_type() == ID_TO_TEST

def test_set_get_eo_ir_type_exceeding_length():
    msg301 = Message301(MSG301_NULL)

    ID_TO_TEST = "valid id valid id valid id valid id"
    assert msg301.set_eo_ir_type(ID_TO_TEST) == False

def test_set_get_eo_ir_type_zero_length():
    msg301 = Message301(MSG301_NULL)

    ID_TO_TEST = ""
    assert msg301.set_eo_ir_type(ID_TO_TEST) == False
