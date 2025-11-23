from .module import Unit


class Meter(Unit):
    unit_type = "length"
    base_units_per = 1.0


class Kilometer(Unit):
    unit_type = "length"
    base_units_per = 1000.0


class Centimeter(Unit):
    unit_type = "length"
    base_units_per = 0.01


class Inch(Unit):
    unit_type = "length"
    base_units_per = 0.0254


class Foot(Unit):
    unit_type = "length"
    base_units_per = 0.3048


class Kilogram(Unit):
    unit_type = "mass"
    base_units_per = 1.0


class Gram(Unit):
    unit_type = "mass"
    base_units_per = 0.001


class Pound(Unit):
    unit_type = "mass"
    base_units_per = 0.45359237


class Second(Unit):
    unit_type = "time"
    base_units_per = 1.0


class Minute(Unit):
    unit_type = "time"
    base_units_per = 60.0
