# -*- coding: utf-8 -*-
from __future__ import absolute_import
from ._utils import api_util, Base


class IError(Base):
    __slots__ = []
    _api_prefix = "Error"
    _columns = ["Description", "Number", "EarlyAbort"]

    def Description(self):
        """(read-only) Description of error for last operation"""
        return self._get_string(self._lib.Error_Get_Description())

    def Number(self):
        """(read-only) Error Number (returns current value and then resets to zero)"""
        return self._lib.Error_Get_Number()

    def EarlyAbort(self, *args):
        """
        EarlyAbort controls whether all errors halts the DSS script processing (Compile/Redirect), defaults to True.

        (API Extension)
    """
        # Getter
        if len(args) == 0:
            return self._lib.Error_Get_EarlyAbort() != 0

        # Setter
        Value, = args
        self._lib.Error_Set_EarlyAbort(Value)

    def ExtendedErrors(self, *args):
        """
        Controls whether the extended error mechanism is used. Defaults to True.

        Extended errors are errors derived from checks across the API to ensure
        a valid state. Although many of these checks are already present in the 
        original/official COM interface, the checks do not produce any error 
        message. An error value can be returned by a function but this value
        can, for many of the functions, be a valid value. As such, the user
        has no means to detect an invalid API call. 

        Extended errors use the Error interface to provide a more clear message
        and should help users, especially new users, to find usage issues earlier.

        At Python level, an exception is raised when an error is detected through
        the Error interface.

        The current default state is ON. For compatibility, the user can turn it
        off to restore the previous behavior.

        (API Extension)

    """
        # Getter
        if len(args) == 0:
            return self._lib.Error_Get_ExtendedErrors() != 0

        # Setter
        Value, = args
        self._lib.Error_Set_ExtendedErrors(Value)


_Error = IError(api_util)

# For backwards compatibility, bind to the default instance
Description = _Error.Description
Number = _Error.Number
EarlyAbort = _Error.EarlyAbort
ExtendedErrors = _Error.ExtendedErrors
_columns = _Error._columns
__all__ = ["Description", "Number", "EarlyAbort", "ExtendedErrors"]
