import unittest


class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

    def count_down(self):
        self.value -= self.step


class TestCount3(unittest.TestCase):
    def test_1(self):
        counter = MyCounterV3(value=0, step=1)
        self.assertEqual(0, counter.value)

    def test_2(self):
        counter = MyCounterV3(value=0, step=1)

        counter.count_up()
        self.assertEqual(1, counter.value)

    def test_3(self):
        counter = MyCounterV3(value=0, step=3)

        counter.count_up()
        counter.count_up()

        self.assertEqual(6, counter.value)

    def test_4(self):
        counter = MyCounterV3(value=1, step=2)

        counter.count_up()
        counter.count_up()
        counter.count_down()

        self.assertEqual(3, counter.value)


if __name__ == '__main__':
    unittest.main()
