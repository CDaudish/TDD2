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
        self.assertFalse(check_pwd("abcabcabcabcabcabcabc"))

    def test6(self):
        self.assertFalse(check_pwd("A123455678"))

    def test7(self):
        self.assertFalse(check_pwd("A123455678"))
    def test8(self):
        self.assertFalse(check_pwd("aB1234567"))

