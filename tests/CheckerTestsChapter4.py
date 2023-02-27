from .BaseCheckerTest import BaseCheckerTest

class CheckerTestsChapter4(BaseCheckerTest):
    CHAPTER_NUM = 4

    """
    Test camel case checks, Check 4.6.1
    """
    def test_camel_case_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadCamelCase.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:2:16: Name 'ThisNotCamel' must match pattern '^[a-z][a-zA-Z0-9]*$'. [MemberName]",
                f"[ERROR] {self.TEST_FILE_PATH}:6:13: Name 'this_should_be_camel_case' must match pattern '^[a-z][a-zA-Z0-9]*$'. [LocalVariableName]",
                f"[ERROR] {self.TEST_FILE_PATH}:9:17: Name 'ThisNeedsToBeCamelCase' must match pattern '^[a-z][a-zA-Z0-9]*$'. [MethodName]"
            ]
        )
    
    """
    Test upper camel case checks, Check 4.6.2
    """
    def test_upper_camel_case_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadUpperCamelCase.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:1:14: Name 'badUpperCamelCase' must match pattern '^[A-Z][a-zA-Z0-9]*$'. [TypeName]",
                f"[ERROR] {self.TEST_FILE_PATH}:2:12: Name 'badUpperCamelCase' must match pattern '^[A-Z][a-zA-Z0-9]*$'. [TypeName]"
            ]
        )

    """
    Test screaming case checks, Check 4.6.3
    """
    def test_screaming_case_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadScreamingCase.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:2:29: Name 'not_screaming_case' must match pattern '\x08[A-Z]+(_[A-Z]+)*\x08'. [ClassConstantName]",
                f"[ERROR] {self.TEST_FILE_PATH}:3:29: Name 'notScreamingCase' must match pattern '\x08[A-Z]+(_[A-Z]+)*\x08'. [ClassConstantName]"
            ]
        )
