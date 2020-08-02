# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ._utils import CheckForError, api_util, Iterable


class IGenerators(Iterable):
    __slots__ = []
    _api_prefix = "Generators"
    _columns = [
        "Name",
        "Idx",
        "ForcedON",
        "Model",
        "Phases",
        "PF",
        "kVARated",
        "kV",
        "kW",
        "kvar",
        "Vminpu",
        "Vmaxpu",
        "RegisterNames",
        "RegisterValues",
    ]

    def ForcedON(self, *args):
        """Indicates whether the generator is forced ON regardles of other dispatch criteria."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_ForcedON()) != 0

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_ForcedON(Value))

    def Model(self, *args):
        """Generator Model"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Model())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Model(Value))

    def PF(self, *args):
        """Power factor (pos. = producing vars). Updates kvar based on present kW value."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_PF())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_PF(Value))

    def Phases(self, *args):
        """Number of phases"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Phases())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Phases(Value))

    def RegisterNames(self):
        """(read-only) Array of Names of all generator energy meter registers"""
        return self.CheckForError(
            self._get_string_array(self._lib.Generators_Get_RegisterNames)
        )

    def RegisterValues(self):
        """(read-only) Array of valus in generator energy meter registers."""
        return self._get_float64_array(self._lib.Generators_Get_RegisterValues)

    def Vmaxpu(self, *args):
        """Vmaxpu for generator model"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Vmaxpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Vmaxpu(Value))

    def Vminpu(self, *args):
        """Vminpu for Generator model"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_Vminpu())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_Vminpu(Value))

    def kV(self, *args):
        """Voltage base for the active generator, kV"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kV())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kV(Value))

    def kVARated(self, *args):
        """kVA rating of the generator"""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kVArated())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kVArated(Value))

    def kW(self, *args):
        """kW output for the active generator. kvar is updated for current power factor."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kW())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kW(Value))

    def kvar(self, *args):
        """kvar output for the active generator. Updates power factor based on present kW value."""
        # Getter
        if len(args) == 0:
            return self.CheckForError(self._lib.Generators_Get_kvar())

        # Setter
        Value, = args
        self.CheckForError(self._lib.Generators_Set_kvar(Value))


_Generators = IGenerators(api_util)

# For backwards compatibility, bind to the default instance
AllNames = _Generators.AllNames
Count = _Generators.Count
First = _Generators.First
ForcedON = _Generators.ForcedON
Model = _Generators.Model
Name = _Generators.Name
Next = _Generators.Next
PF = _Generators.PF
Phases = _Generators.Phases
RegisterNames = _Generators.RegisterNames
RegisterValues = _Generators.RegisterValues
Vmaxpu = _Generators.Vmaxpu
Vminpu = _Generators.Vminpu
Idx = _Generators.Idx
kV = _Generators.kV
kVARated = _Generators.kVARated
kW = _Generators.kW
kvar = _Generators.kvar
_columns = _Generators._columns
__all__ = [
    "AllNames",
    "Count",
    "First",
    "ForcedON",
    "Model",
    "Name",
    "Next",
    "PF",
    "Phases",
    "RegisterNames",
    "RegisterValues",
    "Vmaxpu",
    "Vminpu",
    "Idx",
    "kV",
    "kVARated",
    "kW",
    "kvar",
]
