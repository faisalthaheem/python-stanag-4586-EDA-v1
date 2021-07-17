"""
 Copyright (c) 2021 Faisal Thaheem (https://github.com/faisalthaheem/python-stanag-4586-EDA-v1)
 License GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
"""
from abc import ABC, abstractmethod
import logging
import os
from ctypes import *
from sys import meta_path

class MessageBaseMeta(type(BigEndianStructure), type(ABC)):
    pass

class MessageBase(BigEndianStructure, ABC, metaclass=MessageBaseMeta):

    def __init__(self) -> None:
        super().__init__()

        DEBUG_LEVEL = os.getenv("STANAG4586_EDAV1_DEBUG_LEVEL")
        self._logger = logging.getLogger(type(self).__name__)
        
        if DEBUG_LEVEL is not None:
            self._logger.setLevel(DEBUG_LEVEL)
        else:
            self._logger.setLevel(logging.CRITICAL)


    def set_string_field(self, field_name, field_max_length, field_value):

        if len(field_value) > field_max_length or len(field_value) == 0:
            return False

        setattr(self, field_name, field_value.encode("ascii"))

        return True

    def get_string_field(self, field_name):
        if not hasattr(self, field_name): 
            return

        return bytes(getattr(self, field_name)).decode('ascii')

    def dump(self):
        for field_name, field_type in self._fields_:
            self._logger.debug("{}=[{}]".format(field_name, getattr(self, field_name)))

    @abstractmethod
    def getStationId(self):
        """Returns the station or controlled station field value or None if field is absent"""
        