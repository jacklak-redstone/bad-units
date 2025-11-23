from .module import Unit


class Meter(Unit):
    unit_type: str = "length"
    base_units_per: float = 1.0


class Kilometer(Unit):
    unit_type: str = "length"
    base_units_per: float = 1000.0


class Centimeter(Unit):
    unit_type: str = "length"
    base_units_per: float = 0.01


class Inch(Unit):
    unit_type: str = "length"
    base_units_per: float = 0.0254


class Foot(Unit):
    unit_type: str = "length"
    base_units_per: float = 0.3048


class Kilogram(Unit):
    unit_type: str = "mass"
    base_units_per: float = 1.0


class Gram(Unit):
    unit_type: str = "mass"
    base_units_per: float = 0.001


class Pound(Unit):
    unit_type: str = "mass"
    base_units_per: float = 0.45359237


class Second(Unit):
    unit_type: str = "time"
    base_units_per: float = 1.0


class Minute(Unit):
    unit_type: str = "time"
    base_units_per: float = 60.0
