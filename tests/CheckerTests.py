import unittest
from src.Checker import Checker
from checks.Checks import *

class TestLineLengthChecker(unittest.TestCase):
    def test_line_length_checker_success(self):
        with open("tests/sample_programs/ExcessLineLength.txt") as f:
            actual = Checker(f).evaluation

        expected = {
            0: [LineLengthCheck().message]
        }
        self.assertEqual(actual, expected)
