import unittest


class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1


class TestCount1(unittest.TestCase):
    def test_1(self):
        counter = MyCounterV1(value=0)
        self.assertEqual(0, counter.value)

    def test_2(self):
        counter = MyCounterV1(value=7)
        self.assertEqual(7, counter.value)

    def test_3(self):
        counter = MyCounterV1(value=0)

        counter.count_up()

        self.assertEqual(1, counter.value)

    def test_4(self):
        counter = MyCounterV1(value=0)

        counter.count_up()
        counter.count_up()
        counter.count_up()

        self.assertEqual(3, counter.value)


if __name__ == '__main__':
    unittest.main()
