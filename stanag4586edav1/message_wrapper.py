"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

from ctypes import *
from pprint import pprint

class MessageWrapper(BigEndianStructure):
    
    MSGLEN  = 30
    MSGNULL = b"\x00" * MSGLEN

    _pack_ = 1
    _fields_ = [
        ("idd_version",             c_char*10),
        ("msg_instance_id",         c_uint32),
        ("message_type",            c_uint32),
        ("message_length",          c_uint32),
        ("stream_id",               c_uint32),
        ("message_properties",      c_uint32)
      ]
    def __new__(cls, byte_buffer=None):
        return cls.from_buffer_copy(byte_buffer)

    def __init__(self, byte_buffer=None):
        pass

    def encode(self):
        return bytes(self)

    def dump(self):
        pprint(self)

    def wrap_message(self, instance_id, type, msg, ack_needed):
        encoded_payload = msg.encode()

        self.idd_version = b"\x31\x32"
        self.msg_instance_id = instance_id
        self.message_type = type
        self.message_length = len(encoded_payload)
        self.stream_id = 0
        self.message_properties = 1 if ack_needed else 0

        return self.encode() + encoded_payload