import unittest
from typing import List


class WordFilter:
    def __init__(self, *ng_words):
        self.ng_words = ng_words
        self.replace_word = '<censored>'

    def detect(self, sentence: str) -> bool:
        return any([ng_word in sentence for ng_word in self.ng_words])

        # 内包表記を使わない場合はこんな感じ
        # for ng_word in self.ng_words:
        #     if ng_word in sentence:
        #         return True
        #
        # return False

    def censor(self, sentence: str) -> str:
        if self.detect(sentence):
            for ng_word in self.ng_words:
                sentence = sentence.replace(ng_word, self.replace_word)

        return sentence

    def update_replace_word(self, new_replace_word: str) -> None:
        self.replace_word = new_replace_word

    def initialize_ng_words(self, new_ng_words: List[str]) -> None:
        self.ng_words = new_ng_words


class TestWordFilter(unittest.TestCase):
    def test_課題1_NGワードが含まれているか判定できる(self):
        my_filter = WordFilter('アーセナル')

        with self.subTest('NGワードが含まれている'):
            self.assertTrue(my_filter.detect('ken: 昨日のアーセナルの試合アツかった！'))

        with self.subTest('NGワードが含まれていない'):
            self.assertFalse(my_filter.detect('ken: 昨日のリバプールの試合アツかった！'))

    def test_課題2_NGワードを置き換えることができる(self):
        my_filter = WordFilter('アーセナル')
        actual = my_filter.censor('ken: 昨日のアーセナルの試合アツかった！')
        self.assertEqual('ken: 昨日の<censored>の試合アツかった！', actual)

    def test_課題3_置き換え単語を自由に変更できる(self):
        my_filter = WordFilter('アーセナル')
        my_filter.update_replace_word('<NG>')

        actual = my_filter.censor('ken: 昨日のアーセナルの試合アツかった！')

        self.assertEqual('ken: 昨日の<NG>の試合アツかった！', actual)

    def test_課題4_NGワードの複数登録ができる(self):
        my_filter = WordFilter('アーセナル', '試合')

        actual = my_filter.censor('ken: 昨日のアーセナルの試合アツかった！')

        self.assertEqual('ken: 昨日の<censored>の<censored>アツかった！', actual)

    def test_課題5_NGワードを変更できる(self):
        my_filter = WordFilter('アーセナル', '試合')
        my_filter.initialize_ng_words(['ken', 'アツかった'])

        actual = my_filter.censor('ken: 昨日のアーセナルの試合アツかった！')

        self.assertEqual('<censored>: 昨日のアーセナルの試合<censored>！', actual)


if __name__ == '__main__':
    unittest.main()
