import unittest
from unittest.mock import *
from zad3.src.someclass import SomeClass
from zad3.src.checker import Checker


class TestChecker(unittest.TestCase):
    def test_checker_after_17(self):
        sc = SomeClass()
        sc.getTime = Mock(name='getTime')
        sc.getTime.return_value = 22
        checker = Checker(sc)
        checker.reminder()
        self.assertEqual(checker.sc.wav_was_played, True)

    def test_checker_before_17(self):
        sc = SomeClass()
        sc.getTime = Mock(name='getTime')
        sc.getTime.return_value = 15
        checker = Checker(sc)
        checker.reminder()
        self.assertEqual(checker.sc.wav_was_played, False)
