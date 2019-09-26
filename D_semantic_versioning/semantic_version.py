from __future__ import annotations


class SemanticVersion:
    """バージョンを表現したクラス
    ex:
        Python 3.7.0
        Ruby 2.5.8
        MacOS(HighSierra) 10.13.6
    """

    def __init__(self, major: int, minor: int, patch: int):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self) -> str:
        return f'{self.major}.{self.minor}.{self.patch}'

    def __eq__(self, other: SemanticVersion) -> bool:
        return isinstance(other, SemanticVersion) and \
               (self.major, self.minor, self.patch) == (other.major, other.minor, other.patch)

    def major_version_up(self):
        return SemanticVersion(self.major + 1, 0, 0)

    def minor_version_up(self):
        return SemanticVersion(self.major, self.minor + 1, 0)

    def patch_version_up(self) -> SemanticVersion:
        return SemanticVersion(self.major, self.minor, self.patch + 1)


def main():
    # Python3.7.0 というバージョンを表現したもの
    py370 = SemanticVersion(major=3, minor=7, patch=0)

    # '等価である場合'
    print(SemanticVersion(3, 7, 0) == py370)  # True

    # '等価でない場合'
    print(SemanticVersion(3, 7, 1) != py370)  # True

    # 文字列表現を得られる
    print('3.7.0' == str(py370))  # True

    # パッチバージョンアップができる
    py371 = py370.patch_version_up()
    print(SemanticVersion(3, 7, 1) == py371)  # True

    # マイナーバージョンアップができる
    py380 = py370.minor_version_up()
    print(SemanticVersion(3, 8, 0) == py380)  # True

    # メジャーバージョンアップができる
    py400 = py370.major_version_up()
    print(SemanticVersion(4, 0, 0) == py400)  # True


if __name__ == '__main__':
    main()
