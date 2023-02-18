import unittest
from src.Checker import Checker
from src.checks.Checks import *

class CheckerTestsChapter2(unittest.TestCase):
    PROGRAMS_PATH = "tests/sample_programs/2"

    """
    Test the Wildcard Input Checker, Check 2.1.1
    """
    def test_wildcard_input_checker_success(self):
        with open(f"{self.PROGRAMS_PATH}/NoWildcardImport.java") as f:
            actual = Checker(f).evaluation
        
        expected = {
            0: [WildcardInputCheck().message]
        }
        self.assertEqual(actual, expected)
