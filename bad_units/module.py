import typing


class UnitError(Exception):
    def __init__(self, message: str) -> None:
        self.message: str = message
        super().__init__(self.message)


class Unit:
    unit_type: str = ''
    base_units_per: float = 0.0

    def __init__(self, amount: typing.Union[int, float] = 1):
        if amount < 0:
            raise UnitError("Unit amounts cannot be negative")
        self.amount = amount

    def to(self: Unit, other: Unit) -> Unit:
        if not isinstance(other, Unit):
            raise TypeError("Can only convert to another Unit")
        if self.unit_type != other.unit_type:
            raise UnitError("Units must be of the same type")
        return other.__class__((self.amount * self.base_units_per) / other.base_units_per)

    def __add__(self: Unit, other: typing.Union[Unit, CompoundUnit]) -> typing.Union[Unit, CompoundUnit]:
        if isinstance(other, Unit):
            if self.unit_type != other.unit_type:
                raise UnitError("Units must be of the same type")
            return self.__class__(
                (self.base_units_per * self.amount + other.base_units_per * other.amount) / self.base_units_per
            )
        elif isinstance(other, CompoundUnit):
            return other + self
        else:
            raise TypeError("Can only add Unit or CompoundUnit")

    def __sub__(self: Unit, other: typing.Union[Unit, CompoundUnit]) -> typing.Union[Unit, CompoundUnit]:
        if isinstance(other, Unit):
            if self.unit_type != other.unit_type:
                raise UnitError("Units must be of the same type")
            return self.__class__(
                (self.base_units_per * self.amount - other.base_units_per * other.amount) / self.base_units_per
            )
        elif isinstance(other, CompoundUnit):
            return CompoundUnit(self) - other
        else:
            raise TypeError("Can only subtract Unit or CompoundUnit")

    def __truediv__(self: Unit, other: Unit) -> CompoundUnit:
        return CompoundUnit(self, other)

    def __mul__(self: Unit, other: typing.Union[Unit, CompoundUnit]) -> CompoundUnit:
        if isinstance(other, Unit):
            # Two plain units -> numerator contains both, denominator is None
            return CompoundUnit(self, other)
        elif isinstance(other, CompoundUnit):
            # Multiply Unit with CompoundUnit
            return CompoundUnit(
                numerator=CompoundUnit(self, other.numerator),
                denominator=other.denominator
            )
        else:
            raise TypeError("Can only multiply by Unit or CompoundUnit")

    def __repr__(self: Unit) -> str:
        return f"{self.amount:g} {self.__class__.__name__}"

    def __eq__(self: Unit, other: Unit) -> bool:
        if not isinstance(other, Unit):
            raise UnitError("Units must be of the same type")
        return (
            self.unit_type == other.unit_type
            and self.amount == other.amount
            and self.base_units_per == other.base_units_per
        )


class CompoundUnit:
    def __init__(
            self,
            numerator: typing.Union["Unit", "CompoundUnit"],
            denominator: typing.Union["Unit", "CompoundUnit", None] = None
    ) -> None:
        self.numerator: typing.Union["Unit", "CompoundUnit"] = numerator
        self.denominator: typing.Union["Unit", "CompoundUnit", None] = denominator

    def _check_compatibility(self: CompoundUnit, other: CompoundUnit) -> None:
        if not isinstance(other, CompoundUnit):
            raise TypeError("Can only add/subtract with another CompoundUnit")
        if not isinstance(self.numerator, Unit) or not isinstance(self.denominator, Unit)\
                or not isinstance(other.numerator, Unit) or not isinstance(other.denominator, Unit):
            raise TypeError("Can only add/subtract with another CompoundUnit")
        if self.numerator.unit_type != other.numerator.unit_type:
            raise UnitError("Cannot add/subtract: numerators mismatch")
        if self.denominator and other.denominator:
            if self.denominator.unit_type != other.denominator.unit_type:
                raise UnitError("Cannot add/subtract: denominators mismatch")
        elif (self.denominator is None) != (other.denominator is None):
            raise UnitError("Cannot add/subtract: one has denominator, other does not")

    def __add__(self: CompoundUnit, other: typing.Union[Unit, CompoundUnit]) -> CompoundUnit:
        if isinstance(other, Unit):
            if self.denominator is None:
                return CompoundUnit(self.numerator + other)
            else:
                raise UnitError("Cannot add Unit directly to CompoundUnit with denominator")
        self._check_compatibility(other)
        if self.denominator:
            new_numerator = self.numerator + other.numerator
            return CompoundUnit(new_numerator, self.denominator)
        else:
            new_numerator = self.numerator + other.numerator
            return CompoundUnit(new_numerator)

    def __sub__(self: CompoundUnit, other: typing.Union[Unit, CompoundUnit]) -> CompoundUnit:
        if isinstance(other, Unit):
            if self.denominator is None:
                return CompoundUnit(self.numerator - other)
            else:
                raise UnitError("Cannot subtract Unit directly from CompoundUnit with denominator")
        self._check_compatibility(other)
        if self.denominator:
            new_numerator = self.numerator - other.numerator
            return CompoundUnit(new_numerator, self.denominator)
        else:
            new_numerator = self.numerator - other.numerator
            return CompoundUnit(new_numerator)

    def __truediv__(self: CompoundUnit, other: typing.Union[Unit, CompoundUnit]) -> CompoundUnit:
        if isinstance(other, Unit):
            return CompoundUnit(self.numerator, self.denominator * other if self.denominator else other)
        elif isinstance(other, CompoundUnit):
            return CompoundUnit(self.numerator * other.denominator if other.denominator else self.numerator,
                                self.denominator * other.numerator if self.denominator else other.numerator)
        else:
            raise TypeError("Can only divide by Unit or CompoundUnit")

    def __mul__(self: CompoundUnit, other: typing.Union[Unit, CompoundUnit]) -> CompoundUnit:
        if isinstance(other, Unit):
            return CompoundUnit(self.numerator * other, self.denominator)
        elif isinstance(other, CompoundUnit):
            new_numerator = self.numerator * other.numerator
            new_denominator: typing.Union["Unit", "CompoundUnit", None] = None
            if self.denominator and other.denominator:
                new_denominator = self.denominator * other.denominator
            elif self.denominator:
                new_denominator = self.denominator
            elif other.denominator:
                new_denominator = other.denominator
            return CompoundUnit(new_numerator, new_denominator)
        else:
            raise TypeError("Can only multiply by Unit or CompoundUnit")

    def __repr__(self: CompoundUnit) -> str:
        if self.denominator is None:
            return f"{self.numerator}"
        num_str = f"({self.numerator})" if isinstance(self.numerator, CompoundUnit) else f"{self.numerator}"
        den_str = f"({self.denominator})" if isinstance(self.denominator, CompoundUnit) else f"{self.denominator}"
        return f"{num_str}/{den_str}"

    def __eq__(self: CompoundUnit, other: CompoundUnit) -> bool:
        if not isinstance(other, CompoundUnit):
            raise UnitError("Units must be of the same type")
        return (
            self.numerator == other.numerator
            and self.denominator == other.denominator
        )

# Probably self.numerator & self.denominator are not correctly implemented
# As of my understanding, they can also be CompoundUnit, and not only Unit
# Which just breaks everything :joy:
