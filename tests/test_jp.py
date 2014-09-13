#coding: utf-8
import unittest
import pytest
from jp_token_preprocessing import JpTokenPreprocessing

class TestLength(unittest.TestCase):
    def setUp(self):
        self.preprocessesor = JpTokenPreprocessing(min_len=2)
        token = ['木', '水']
        expect = []
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

        self.preprocessesor.min_len = 1
        token = ['木', '水']
        expect = ['木', '水']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

class TestUnicodeNormalize(unittest.TestCase):
    def setUp(self):
        self.preprocessesor = JpTokenPreprocessing(number=True, case='lower', unicode='NFKC', min_len=2)

    def test_alphabet_num(self):
        token = ['１２３', 'ＡＢＣ', 'ＡＢ１']
        expect = ['123', 'abc', 'ab1']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

    def test_symbol(self):
        self.preprocessesor.symbol = True
        token = ['！？', 'ＡＢＣ？']
        expect = ['!?', 'abc?']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

if __name__ == '__main__':
    unittest.main()
