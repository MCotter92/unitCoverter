import sys
import os
import pytest

main_dir = os.path.abspath(
    "/Users/mason_cotter/Desktop/python_projects/UnitsConverter/unitsconverter"
)
sys.path.append(main_dir)

from Converter import Converter

c = Converter(inch=10, cm=25.4, m=0.5)


def test_int_to_ft():
    assert type(c.convert("inch", "ft")) == float


def test_inches_to_cm():
    c = Converter(inch=10)
    assert c.convert("inch", "cm") == 25.4


def test_cm_to_inches():
    c = Converter(cm=25.4)
    assert c.convert("cm", "inch") == 10.0


def test_m_to_inches():
    c = Converter(m=0.5)
    assert c.convert("m", "inch") == 19.685
