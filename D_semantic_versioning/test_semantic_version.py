import unittest

from Day02_20190924_Webプログラミング.lecture.oop.semantic_versioning.semantic_version import SemanticVersion


class TestVersion(unittest.TestCase):
    def setUp(self) -> None:
        self.py370 = SemanticVersion(3, 7, 0)
        self.high_sierra_version = SemanticVersion(10, 13, 6)

    def test_等価性の比較ができる(self):
        with self.subTest('等価である場合'):
            self.assertTrue(SemanticVersion(3, 7, 0) == self.py370)

        with self.subTest('等価でない場合'):
            self.assertTrue(SemanticVersion(2, 7, 0) != self.py370)

    def test_文字列表現を得られる(self):
        with self.subTest('Python 3.7.0'):
            self.assertEqual('3.7.0', str(self.py370))

        with self.subTest('High Sierra 10.13.6'):
            self.assertEqual('10.13.6', str(self.high_sierra_version))

    def test_パッチバージョンアップができる(self):
        with self.subTest('Python 3.7.0 -> 3.7.1'):
            self.assertEqual(SemanticVersion(3, 7, 1), self.py370.patch_version_up())

        with self.subTest('High Sierra 10.13.6 -> 10.13.7'):
            self.assertEqual(SemanticVersion(10, 13, 7), self.high_sierra_version.patch_version_up())

    def test_マイナーバージョンアップができる(self):
        with self.subTest('Python 3.7.0 -> 3.8.0'):
            self.assertEqual(SemanticVersion(3, 8, 0), self.py370.minor_version_up())

        with self.subTest('High Sierra 10.13.6 -> 10.14.0'):
            self.assertEqual(SemanticVersion(10, 14, 0), self.high_sierra_version.minor_version_up())

    def test_メジャーバージョンアップができる(self):
        with self.subTest('Python 3.7.0 -> 4.0.0'):
            self.assertEqual(SemanticVersion(4, 0, 0), self.py370.major_version_up())

        with self.subTest('High Sierra 10.13.6 -> 11.0.0'):
            self.assertEqual(SemanticVersion(11, 0, 0), self.high_sierra_version.major_version_up())


if __name__ == "__main__":
    unittest.main()
