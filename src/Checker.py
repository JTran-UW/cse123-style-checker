from .checks.Check import Check
from .checks.Checks import *
from typing import *

class Checker:
    """
    Checker TODO
    """
    def __init__(self, file: TextIO):
        self.file: TextIO = file
        self.registered_checks: list[Check] = [LineLengthCheck()]
        self.evaluation: Dict[int, list[str]] = self._evaluate_file(file)
    
    """
    Evaluate a file line-by-line with all registered checks

    :param file: file to evaluate
    :returns: mapping of line number to issue messages
    """
    def _evaluate_file(self, file: TextIO) -> Dict[int, list[str]]:
        issues: Dict[int, list[str]] = {}

        for n, line in enumerate(file):
            for check in self.registered_checks:
                # Check validity of line
                if not check.evaluate_line(line):
                    if n in issues.keys():
                        issues[n].append(check.message)
                    else:
                        issues[n] = [check.message]
        
        return issues


