"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message302 import *


PACKET_TO_DECODE = b"\x00\x00\x00\x00\x00\x00\x00\x00" \
b"\x00\x00\x00\x50" \
b"\x00\x00\x00\xA0" \
b"\x00\x00\x00\x00" \
b"\x00\x00\x00\x08" \
b"\x01" \
b"\x05" \
b"\x01" \
b"\x01" \
b"\x03" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x01" \
b"\x40\x40\x80\x00\x00\x00\x00\x00" \
b"\x40\x40\x80\x00\x00\x00\x00\x00" \
b"\x3f\x80\x00\x00" \
b"\x01" \
b"\x01" \
b"\x3f\x80\x00\x00" \
b"\x01" \
b"\x01" \
b"\x01" \
b"\x00\x01" \
b"\x01" 

def test_decode_message302():
    msg302 = Message302(PACKET_TO_DECODE)
    
    assert msg302.time_stamp == 0x00
    assert msg302.vehicle_id == 0x50
    assert msg302.cucs_id == 0xA0
    assert msg302.vsm_id == 0x00
    assert msg302.station_number == 0x08
    assert msg302.addressed_sensor == Message302_addressed_sensor.EO
    assert msg302.system_operating_mode_state == Message302_system_operating_mode_state.ACTIVE
    assert msg302.eo_sensor_mode_status == Message302_eo_sensor_mode_status.COLOR_MODE
    assert msg302.ir_polarity_status == Message302_ir_polarity_status.WHITE_HOT
    assert msg302.image_output_state == Message302_image_output_state.BOTH
    assert msg302.actual_centerline_elevation_angle == 1.0
    assert msg302.actual_vertical_field_of_view == 1.0
    assert msg302.actual_centerline_azimuth_angle == 1.0
    assert msg302.actual_horizontal_field_of_view == 1.0
    assert msg302.actual_sensor_rotation_angle == 1.0
    assert msg302.image_position == 1
    assert msg302.latitude == 33.0
    assert msg302.longitude == 33.0
    assert msg302.altitude == 1.0
    assert msg302.pointing_mode_state == Message302_pointing_mode_state.ANGLE_RELATIVE_TO_UA
    assert msg302.preplan_mode == Message302_preplan_mode.OPERATE_IN_PREPLAN_MODE
    assert msg302.reported_range == 1.0
    assert msg302.fire_laser_pointer_status == Message302_fire_laser_pointer_status.ON_SAFED
    assert msg302.fire_laser_rangefinder_status == Message302_fire_laser_rangefinder_status.ON_SAFED
    assert msg302.selected_laser_rangefinder_first_last_pulse == Message302_selected_laser_rangefinder_first_last_pulse.FIRST
    assert msg302.laser_designator_code == 0x01
    assert msg302.laser_designator_status == Message302_laser_designator_status.ON
 

def test_encode_message302():
    msg302 = Message302(MSG302_NULL)

    msg302.time_stamp = 0x00
    msg302.vehicle_id = 0x50
    msg302.cucs_id = 0xA0
    msg302.vsm_id = 0x00
    msg302.station_number = 0x08
    msg302.addressed_sensor = Message302_addressed_sensor.EO
    msg302.system_operating_mode_state = Message302_system_operating_mode_state.ACTIVE
    msg302.eo_sensor_mode_status = Message302_eo_sensor_mode_status.COLOR_MODE
    msg302.ir_polarity_status = Message302_ir_polarity_status.WHITE_HOT
    msg302.image_output_state = Message302_image_output_state.BOTH
    msg302.actual_centerline_elevation_angle = 1.0
    msg302.actual_vertical_field_of_view = 1.0
    msg302.actual_centerline_azimuth_angle = 1.0
    msg302.actual_horizontal_field_of_view = 1.0
    msg302.actual_sensor_rotation_angle = 1.0
    msg302.image_position = 1
    msg302.latitude = 33.0
    msg302.longitude = 33.0
    msg302.altitude = 1.0
    msg302.pointing_mode_state = Message302_pointing_mode_state.ANGLE_RELATIVE_TO_UA
    msg302.preplan_mode = Message302_preplan_mode.OPERATE_IN_PREPLAN_MODE
    msg302.reported_range = 1.0
    msg302.fire_laser_pointer_status = Message302_fire_laser_pointer_status.ON_SAFED
    msg302.fire_laser_rangefinder_status = Message302_fire_laser_rangefinder_status.ON_SAFED
    msg302.selected_laser_rangefinder_first_last_pulse = Message302_selected_laser_rangefinder_first_last_pulse.FIRST
    msg302.laser_designator_code = 0x01
    msg302.laser_designator_status = Message302_laser_designator_status.ON

    assert msg302.encode() == PACKET_TO_DECODE