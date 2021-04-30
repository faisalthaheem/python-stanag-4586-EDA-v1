"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from stanag4586edav1.message_wrapper import *

PACKET_TO_DECODE = b"\x32\x2e\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xAA\x00\x00" \
b"\x00\x01\x00\x00\x00\xCC\x00\x00\x00\xBB\x00\x00\x00\xAA"

def test_decode_wrapper():
    wrapper = MessageWrapper(PACKET_TO_DECODE)
    assert wrapper.idd_version == b"\x32\x2e\x30"
    assert wrapper.msg_instance_id == 0xAA
    assert wrapper.message_type == 0x1
    assert wrapper.message_length == 0xCC
    assert wrapper.stream_id == 0xBB
    assert wrapper.message_properties == 0xAA

def test_encode_wrapper():
    wrapper = MessageWrapper(MESSAGE_WRAPPER_NULL)
    
    assert wrapper.msg_instance_id == 0x00

    wrapper.idd_version = b"\x32\x2e\x30"
    wrapper.msg_instance_id = 0xAA
    wrapper.message_type = 0x1
    wrapper.message_length = 0xCC
    wrapper.stream_id = 0xBB
    wrapper.message_properties = 0xAA

    assert wrapper.encode() == PACKET_TO_DECODE