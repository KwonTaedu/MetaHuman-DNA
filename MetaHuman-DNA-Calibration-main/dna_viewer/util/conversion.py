from math import pi

from ..config.units import AngleUnit, LinearUnit
from ..util.error import DNAViewerError


class Conversion:
    
    @staticmethod
    def calculate_linear_modifier(unit, dna_unit = None):
        if dna_unit is None:
            return 1

        if unit != dna_unit:
            if unit == LinearUnit.m:
                return 0.01
            if unit == LinearUnit.cm:
                return 100
        return 1

    @staticmethod
    def calculate_angle_modifier(unit, dna_unit = None):
        if dna_unit is None:
            return 1

        if unit != dna_unit:
            if unit == AngleUnit.degree:
                return 180 / pi
            if unit == AngleUnit.radian:
                return pi / 180
        return 1

    @staticmethod
    def get_linear_unit_from_int(value):
        if value == 0:
            return LinearUnit.cm
        if value == 1:
            return LinearUnit.m
        raise DNAViewerError("Unknown linear unit set in DNA file! value"+value)

    @staticmethod
    def get_angle_unit_from_int(value) :

        if value == 0:
            return AngleUnit.degree
        if value == 1:
            return AngleUnit.radian
        raise DNAViewerError("Unknown linear unit set in DNA file! value"+value)
