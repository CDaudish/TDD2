import unittest
import random
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        self.assertFalse(check_pwd("a"))

    def test2(self):
        self.assertFalse(check_pwd("abcdefg"))

    def test3(self):
        self.assertFalse(check_pwd("abc"))

    def test4(self):
        self.assertFalse(check_pwd("abcabcabcabcabcabcabcabc"))

    def test5(self):
        self.assertFalse(check_pwd("abcabcabcabcabcabcabca"))


