from .BaseCheckerTest import BaseCheckerTest

class CheckerTestsChapter2(BaseCheckerTest):
    CHAPTER_NUM = 2

    """
    Test the Wildcard Input Checker, Check 2.1.1
    """
    def test_wildcard_input_checker_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/NoWildcardImport.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:1:17: import.starImport [StarImport]"]
        )
