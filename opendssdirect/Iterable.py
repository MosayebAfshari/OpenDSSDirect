# -*- coding: utf-8 -*-
from __future__ import absolute_import
from dss._cffi_api_util import Base as DSSPyBase

class Base(DSSPyBase):
    
    def __init__(self, api_util):
        DSSPyBase.__init__(self, api_util)

        # For backwards compatibility. May change according to 
        # https://github.com/dss-extensions/OpenDSSDirect.py/issues/60
        # which would just make the Base class the same for dsspy and oddpy
        self._get_float64_array = api_util.get_float64_array2
        self._get_int32_array = api_util.get_int32_array2
        self._get_int8_array = api_util.get_int8_array2
        self._get_string_array = api_util.get_string_array2
        
        

class Iterable(Base):
    '''Based on dss_python's Iterable class.''' 

    __slots__ = [
        '_Get_First',
        '_Get_Next',
        '_Get_Count',
        '_Get_AllNames',
        '_Get_Name',
        '_Set_Name',
        '_Get_idx',
        '_Set_idx'
    ]
    
    def __init__(self, api_util):
        Base.__init__(self, api_util)
        
        prefix = self._api_prefix
        self._Get_First = getattr(self._lib, '{}_Get_First'.format(prefix))
        self._Get_Next = getattr(self._lib, '{}_Get_Next'.format(prefix))
        self._Get_Count = getattr(self._lib, '{}_Get_Count'.format(prefix))
        self._Get_AllNames = getattr(self._lib, '{}_Get_AllNames'.format(prefix))
        self._Get_Name = getattr(self._lib, '{}_Get_Name'.format(prefix))
        self._Set_Name = getattr(self._lib, '{}_Set_Name'.format(prefix))
        self._Get_idx = getattr(self._lib, '{}_Get_idx'.format(prefix))
        self._Set_idx = getattr(self._lib, '{}_Set_idx'.format(prefix))

    def First(self):
        '''Sets the first object of this type active. Returns 0 if none.'''
        return self._Get_First()

    def Next(self):
        '''(read-only) Sets next object of this type active. Returns 0 if no more.'''
        return self._Get_Next()

    def Count(self):
        '''Number of objects of this type'''
        return self._Get_Count()

    def __len__(self):
        return self._Get_Count()

    def __iter__(self):
        idx = self._Get_First()
        while idx != 0:
            yield self
            idx = self._Get_Next()

    def AllNames(self):
        '''Array of all names of this object type'''
        return self._get_string_array(self._Get_AllNames)

    def Name(self, *args):
        '''Gets the current name or sets the active object of this type by name'''
        # Getter
        if len(args) == 0:
            return self._get_string(self._Get_Name())
        
        # Setter
        Value, = args        
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self.CheckForError(self._Set_Name(Value))
        
    def Idx(self, *args):
        '''Gets the current index or sets the active object of this type by index'''
        # Getter
        if len(args) == 0:
            return self._Get_idx()

        # Setter
        Value, = args        
        if type(Value) is not bytes:
            self.CheckForError(self._Set_idx(Value))

__all__ = ["Iterable"]