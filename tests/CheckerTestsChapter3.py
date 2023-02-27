from .BaseCheckerTest import BaseCheckerTest

class CheckerTestsChapter3(BaseCheckerTest):
    CHAPTER_NUM = 3

    """
    Test indentation checks, Check 3.1.1-3
    """
    def test_indentantion_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadIndentation.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:2:1: 'method def modifier' has incorrect indentation level 0, expected level should be 4. [Indentation]",
                f"[ERROR] {self.TEST_FILE_PATH}:4:8: 'method def' child has incorrect indentation level 7, expected level should be 8. [Indentation]",
                f"[ERROR] {self.TEST_FILE_PATH}:6:5: 'class def rcurly' has incorrect indentation level 4, expected level should be 0. [Indentation]"
            ]
        )

    """
    Test class header spacing checks, Check 3.2.1
    """
    def test_class_header_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadClassHeaderSpacing.java",
            [
                "[ERROR] " + self.TEST_FILE_PATH + ":1:37: '{' is not preceded with whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:7:21: Use a single space to separate non-whitespace characters. [SingleSpaceSeparator]",
                "[ERROR] " + self.TEST_FILE_PATH + ":14:1: '{' at column 1 should be on the previous line. [LeftCurly]"
            ]
        )

    """
    Test method header spacing checks, Check 3.2.2
    """
    def test_method_header_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadMethodHeaderSpacing.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:2:29: '(' is preceded with whitespace. [MethodParamPad]",
                f"[ERROR] {self.TEST_FILE_PATH}:2:39: ',' is not followed by whitespace. [WhitespaceAfter]",
                f"[ERROR] {self.TEST_FILE_PATH}:2:50: ')' is preceded with whitespace. [ParenPad]",
                "[ERROR] " + self.TEST_FILE_PATH + ":2:51: '{' is not preceded with whitespace. [WhitespaceAround]"
            ]
        )
    
    """
    Test method call spacing checks, Check 3.2.3
    """
    def test_method_call_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadMethodCallSpacing.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:3:16: ',' is not followed by whitespace. [WhitespaceAfter]",
                f"[ERROR] {self.TEST_FILE_PATH}:3:19: ')' is preceded with whitespace. [ParenPad]"
            ]
        )
    
    """
    Test loop statement spacing checks, Check 3.2.4
    """
    def test_loop_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadLoopStatementSpacing.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:5:9: 'for' is not followed by whitespace. [WhitespaceAfter]",
                f"[ERROR] {self.TEST_FILE_PATH}:5:18: '=' is not preceded with whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:5:21: ';' is not followed by whitespace. [WhitespaceAfter]",
                f"[ERROR] {self.TEST_FILE_PATH}:5:34: ')' is preceded with whitespace. [ParenPad]",
                f"[ERROR] {self.TEST_FILE_PATH}:10:9: 'while' is not followed by whitespace. [WhitespaceAfter]",
                f"[ERROR] {self.TEST_FILE_PATH}:10:17: '==' is not followed by whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:15:22: ':' is not preceded with whitespace. [WhitespaceAround]"
            ]
        )
    
    """
    Test array spacing checks, Check 3.2.5
    """
    def test_array_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadArraySpacing.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:3:38: ',' is not followed by whitespace. [WhitespaceAfter]"]
        )
    
    """
    Test variable initialization spacing checks, Check 3.2.6
    """
    def test_variable_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadVariableSpacing.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:3:23: '=' is not followed by whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:3:23: '=' is not preceded with whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:4:29: ';' is preceded with whitespace. [NoWhitespaceBefore]"
            ]
        )
    
    """
    Test expression spacing checks, Check 3.2.7
    """
    def test_expression_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadExpressionSpacing.java",
            [
                f"[ERROR] {self.TEST_FILE_PATH}:3:18: '*' is not preceded with whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:3:28: '-' is not followed by whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:4:31: '&&' is not preceded with whitespace. [WhitespaceAround]",
                f"[ERROR] {self.TEST_FILE_PATH}:4:39: '||' is not preceded with whitespace. [WhitespaceAround]"
            ]
        )
    
    """
    Test newline before method comment checks, Check 3.2.8
    """
    def test_method_comment_spacing_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/BadMethodCommentSpacing.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:8:5: 'METHOD_DEF' should be separated from previous line. [EmptyLineSeparator]"]
        )

    """
    Test one statement per line check, Check 3.3.1
    """
    def test_one_statement_line_check_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/MultipleStatementLine.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:3:35: Only one statement per line allowed. [OneStatementPerLine]"]
        )

    """
    Test the line length check, Check 3.4.1
    """
    def test_line_length_checker_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/ExcessLineLength.java", 
            [f"[ERROR] {self.TEST_FILE_PATH}:2: Line is longer than 100 characters (found 107). [LineLength]"]
        )
    
    """
    Test line-wrapping indent check, Check 3.4.2
    """
    def test_line_wrapping_indent_checker_success(self):
        self.base_test_check_success(
            f"{self.CHAPTER_NUM}/NoIndentAfterLineWrap.java",
            [f"[ERROR] {self.TEST_FILE_PATH}:3:5: 'String' has incorrect indentation level 4, expected level should be 8. [Indentation]"]
        )
