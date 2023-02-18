import unittest
from src.Checker import Checker
from src.checks.Checks import *

class CheckerTestsChapter3(unittest.TestCase):
    PROGRAMS_PATH = "tests/sample_programs/3"

    """
    Test the 
    """
    def test_open_brace_indent(self):
        with open(f"")

    """
    Test the Line Length Checker, Check 3.4.1
    """
    def test_line_length_checker_success(self):
        with open(f"{self.PROGRAMS_PATH}/ExcessLineLength.java") as f:
            actual = Checker(f).evaluation

        expected = {
            0: [LineLengthCheck().message]
        }
        self.assertEqual(actual, expected)
