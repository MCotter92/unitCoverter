import math
import pretty_errors


class Convert:
    """
    A class to convert between some basic units of measurement.
    """

    @classmethod
    def __init__(self, inch, ft, cm, m, yd):
        self.inch = inch
        self.ft = ft
        self.cm = cm
        self.m = m
        self.yd = yd

    @classmethod
    def in_to_ft(self) -> float:
        feet = self.inch / 12
        return feet

    @classmethod
    def in_to_cm(self) -> float:
        cent = self.inches * 2.54
        return cent

    @classmethod
    def in_to_meters(self) -> float:
        meters = self.inches / 39.37
        return meters

    @classmethod
    def in_to_yards(self) -> float:
        yards = self.inch / 36
        return yards

    @classmethod
    def feet_to_inches(self) -> float:
        inches = self.feet * 12
        return inches

    @classmethod
    def feet_to_cm(self) -> float:
        cent = self.feet * 30.48
        return cent

    @classmethod
    def feet_to_meters(self) -> float:
        meters = self.feet / 3.281
        return meters

    @classmethod
    def feet_to_yards(self) -> float:
        yards = self.feet / 3
        return yards

    @classmethod
    def cm_to_in(self) -> float:
        inches = self.cm / 2.54
        return inches

    @classmethod
    def cm_to_feet(self) -> float:
        feet = self.cm / 30.48
        return feet

    @classmethod
    def cm_to_meters(self) -> float:
        meters = self.cm / 100
        return meters

    @classmethod
    def cm_to_yards(self) -> float:
        yards = self.cm / 91.44
        return yards

    @classmethod
    def meters_to_inches(self) -> float:
        inches = self.meters * 39.37
        return inches

    @classmethod
    def meters_to_feet(self) -> float:
        feet = self.meters * 3.281
        return feet

    @classmethod
    def meters_to_cm(self) -> float:
        cm = self.meters * 100
        return cm

    @classmethod
    def meters_to_yards(self) -> float:
        yards = self.meters * 1.094
        return yards

    @classmethod
    def yards_to_inches(self) -> float:
        inches = self.yards * 36
        return inches

    @classmethod
    def yards_to_feet(self) -> float:
        feet = self.yards * 3
        return feet

    @classmethod
    def yards_to_cm(self) -> float:
        cm = self.yards * 91.44
        return cm

    @classmethod
    def yards_to_meters(self) -> float:
        meters = self.yards / 1.094
        return meters
