from .BaseCheckerTest import BaseCheckerTest

class CheckerTestsChapter4(BaseCheckerTest):
    CHAPTER_NUM = 4

    """
    Test field private and public checks, Check 4.1.2
    Note: this also tests the class constant check, Check 4.2.1
    """
    def test_wildcard_input_checker_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/FieldsNotPrivate.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:6:5: field notInSpec is public, should be private. [FieldSpecification]",
                f"[ERROR] {self.TEST_FILE_PATH}:17:9: field left is private, should be public. [FieldSpecification]"
            ],
            check_name="specs/tests/4.1.2_checks"
        )

    """
    Test spec method public checks, Check 4.3.1
    """
    def test_wildcard_input_checker_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/SpecMethodNotPublic.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:6:5: method anotherMethod is private, should be public. [MethodSpecification]"],
            check_name="specs/tests/4.3.1_checks"
        )

    """
    Test non-spec method private checks, Check 4.3.2
    """
    def test_wildcard_input_checker_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/NonSpecMethodNotPrivate.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:3:5: method test2 is public, should be private. [MethodSpecification]"],
            check_name="specs/tests/4.3.2_checks"
        )

    """
    Test no extra parameter method checks, Check 4.3.3
    """
    def test_wildcard_input_checker_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/UnnecessaryParams.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:10:5: method test1 is \"String myParam\", should be \" \". [MethodSpecification]"],
            check_name="specs/tests/4.3.3_checks"
        )

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
