#coding: utf-8
import unittest
import pytest
from jp_token_preprocessing import JpTokenPreprocessing

class TestLength(unittest.TestCase):
    def setUp(self):
        self.preprocessesor = JpTokenPreprocessing(min_len=2)
        token = ['a', 'ab']
        expect = ['ab']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

        self.preprocessesor.min_len = 1
        token = ['a', 'ab']
        expect = ['a', 'ab']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

class TestAlphabet(unittest.TestCase):
    def setUp(self):
        self.preprocessesor = JpTokenPreprocessing(number=False, case='lower', min_len=2)

    def test_case_lower(self):
        token = ['ab', 'ABC', 'AbC']
        expect = ['ab', 'abc', 'abc']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

    def test_case_upper(self):
        self.preprocessesor.case = 'upper'
        token = ['ab', 'ABC', 'AbC']
        expect = ['AB', 'ABC', 'ABC']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

    def test_case_capitalize(self):
        self.preprocessesor.case = 'capitalize'
        token = ['ab', 'ABC', 'AbC']
        expect = ['Ab', 'Abc', 'Abc']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

    def test_number(self):
        token = ['12', 'A1', '1v1']
        expect = ['a1', '1v1']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

    def test_symbol(self):
        token = ['!?', 'A!', 'wow!']
        expect = ['a!', 'wow!']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

class TestNumber(unittest.TestCase):
    def setUp(self):
        self.preprocessesor = JpTokenPreprocessing(number=True, min_len=2)

    def test_number(self):
        token = ['12', 'ab', 'A1', '1v1']
        expect = ['12', 'ab', 'a1', '1v1']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

    def test_symbol(self):
        token = ['!?', '12!', '[1]']
        expect = ['12!', '[1]']
        got = list(self.preprocessesor.preprocessing(token))
        assert got == expect

if __name__ == '__main__':
    unittest.main()
