class Converter:
    """
    A class to convert between some basic units of measurement.
    """

    def __init__(self, **units):
        self.units = units

    def convert(self, from_unit, to_unit) -> float:
        conversion_factors = {
            "inch_to_ft": 1 / 12,
            "inch_to_cm": 2.54,
            "inch_to_m": 1 / 39.37,
            "inch_to_yd": 1 / 36,
            "ft_to_inch": 12,
            "ft_to_cm": 30.48,
            "ft_to_m": 1 / 3.281,
            "ft_to_yd": 1 / 3,
            "cm_to_inch": 1 / 2.54,
            "cm_to_ft": 1 / 30.48,
            "cm_to_m": 1 / 100,
            "cm_to_yd": 1 / 91.44,
            "m_to_inch": 39.37,
            "m_to_ft": 3.281,
            "m_to_cm": 100,
            "m_to_yd": 1.094,
            "yd_to_inch": 36,
            "yd_to_ft": 3,
            "yd_to_cm": 91.44,
            "yd_to_m": 1.094,
        }

        if from_unit == to_unit:
            return round(self.units.get(from_unit, 0), 5)

        conversion_key = f"{from_unit}_to_{to_unit}"
        factor = conversion_factors.get(conversion_key)
        if factor is None:
            raise ValueError("Conversion not supported")

        return round(self.units[from_unit] * factor, 5)


c = Converter(inch=10, cm=25.4, m=0.5)
print(c.convert("m", "inch"))
