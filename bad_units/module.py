import typing


class UnitType:
    def __init__(self, factor: typing.Union[int, float]) -> None:
        self.factor: float = factor


class BaseUnitType:
    def __init__(self, category: str) -> None:
        self.category: str = category

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BaseUnitType):
            return NotImplemented
        return self.category == other.category


class Unit:
    unit_type: UnitType
    base_unit_type: BaseUnitType  # Length, Mass, Time, etc.

    def __init__(self, amount: typing.Union[int, float]):
        amount = float(amount)
        self.amount: float = amount
