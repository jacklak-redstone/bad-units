from .module import Unit, BaseUnitType, UnitType


# Base Unit Types

class Length(BaseUnitType):
    category: str = 'length'


class Time(BaseUnitType):
    category: str = 'time'


class Mass(BaseUnitType):
    category: str = 'mass'


class Meter(Unit):
    unit_type: UnitType = UnitType(1.0)
    base_unit_type: BaseUnitType = BaseUnitType(Length.category)


class Kilometer(Unit):
    unit_type: UnitType = UnitType(1000.0)
    base_unit_type: BaseUnitType = BaseUnitType(Length.category)


class Centimeter(Unit):
    unit_type: UnitType = UnitType(0.01)
    base_unit_type: BaseUnitType = BaseUnitType(Length.category)


class Inch(Unit):
    unit_type: UnitType = UnitType(0.0254)
    base_unit_type: BaseUnitType = BaseUnitType(Length.category)


class Foot(Unit):
    unit_type: UnitType = UnitType(0.3048)
    base_unit_type: BaseUnitType = BaseUnitType(Length.category)


class Kilogram(Unit):
    unit_type: UnitType = UnitType(1.0)
    base_unit_type: BaseUnitType = BaseUnitType(Mass.category)


class Gram(Unit):
    unit_type: UnitType = UnitType(0.001)
    base_unit_type: BaseUnitType = BaseUnitType(Mass.category)


class Pound(Unit):
    unit_type: UnitType = UnitType(0.45359237)
    base_unit_type: BaseUnitType = BaseUnitType(Mass.category)


class Second(Unit):
    unit_type: UnitType = UnitType(1.0)
    base_unit_type: BaseUnitType = BaseUnitType(Time.category)


class Minute(Unit):
    unit_type: UnitType = UnitType(60.0)
    base_unit_type: BaseUnitType = BaseUnitType(Time.category)
