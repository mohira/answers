import math
import unittest


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        area = (self.radius ** 2) * math.pi

        return round(area, 2)

    def perimeter(self) -> float:
        perimeter = 2 * math.pi * self.radius

        return round(perimeter, 2)


class TestCircle(unittest.TestCase):
    def test_円の面積を小数点第2位の精度で求めることができる(self):
        with self.subTest('半径が1の円'):
            self.assertEqual(3.14, Circle(radius=1).area())

        with self.subTest('半径が3の円'):
            self.assertEqual(28.27, Circle(radius=3).area())

    def test_円の円周の長さを小数点第2位の精度で求めることができる(self):
        with self.subTest('半径が1の円'):
            self.assertEqual(6.28, Circle(radius=1).perimeter())

        with self.subTest('半径が3の円'):
            self.assertEqual(18.85, Circle(radius=3).perimeter())


if __name__ == '__main__':
    unittest.main()
