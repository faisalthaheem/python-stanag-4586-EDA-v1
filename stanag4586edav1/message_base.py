"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""

class MessageBase:
    """a convenience field to help filter messages at other stages"""
    has_station_number_field = False

    def set_string_field(self, field_name, field_max_length, field_value):

        if len(field_value) > field_max_length or len(field_value) == 0:
            return False

        setattr(self, field_name, field_value.encode("ascii"))

        return True

    def get_string_field(self, field_name):
        if not hasattr(self, field_name): 
            return

        return bytes(getattr(self, field_name)).decode('ascii')