import math
import unittest


class Square:
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        area = self.side ** 2

        return round(area, 2)

    def diagonal(self) -> float:
        diagonal = math.sqrt(self.side ** 2 + self.side ** 2)

        return round(diagonal, 2)


class TestSquare(unittest.TestCase):
    def test_正方形の面積を小数点第2位の精度で求めることができる(self):
        self.assertEqual(9.00, Square(side=3).area())

    def test_正方形の対角線の長さを小数点第2位の精度で求めることができる(self):
        self.assertEqual(1.41, Square(side=1).diagonal())


if __name__ == '__main__':
    unittest.main()
