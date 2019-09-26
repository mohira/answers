import math
import unittest


class Rectangle:
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width

    def area(self) -> float:
        area = self.height * self.width

        return round(area, 2)

    def diagonal(self) -> float:
        diagonal = math.sqrt(self.height ** 2 + self.width ** 2)

        return round(diagonal, 2)


class TestRectangle(unittest.TestCase):
    def test_長方形の面積を小数点第2位の精度で求めることができる(self):
        with self.subTest('その1'):
            self.assertEqual(30.00, Rectangle(height=5, width=6).area())

        with self.subTest('その2'):
            self.assertEqual(9.00, Rectangle(height=3, width=3).area())

    def test_長方形の対角線の長さを小数点第2位の精度で求めることができる(self):
        with self.subTest('その1'):
            self.assertEqual(7.81, Rectangle(height=5, width=6).diagonal())

        with self.subTest('その2'):
            self.assertEqual(4.24, Rectangle(height=3, width=3).diagonal())


if __name__ == '__main__':
    unittest.main()
