import unittest
from bad_units.builtin_units import Meter, Centimeter, Second
from bad_units.module import CompoundUnit


class MyTestCase(unittest.TestCase):
    def test_something(self) -> None:
        self.assertEqual(Meter(2), Meter(1) + Centimeter(100))

        # Compound units
        self.assertEqual(CompoundUnit(Meter(10), Second(2)), Meter(10) / Second(2))
        self.assertEqual(CompoundUnit(Meter(10), Second(2) * Second(5)), (Meter(10) / Second(2)) / Second(5))

        # Adding compatible compound units
        # speed2 = Centimeter(200) / Second(2)
        # print(speed + speed2)


if __name__ == '__main__':
    unittest.main()
