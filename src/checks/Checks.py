from .Check import Check

class LineLengthCheck(Check):
    """
    Line Length Check TODO
    """
    def __init__(self):
        message: str = "Line exceeds 100 characters."
        super().__init__(message)
    
    # Override
    def evaluate_line(self, line: str) -> bool:
        return len(line) < 100
