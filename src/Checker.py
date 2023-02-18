from typing import *
import subprocess

class Checker:
    """
    File Checker, evaluates file on all registered checks

    :param file: open read-permissioned file object
    """
    def __init__(self, checkstyle_jar: str, config: str):
        self.checkstyle_jar = checkstyle_jar
        self.config = config
    
    """
    Evaluate a file line-by-line with all registered checks

    :param file: file to evaluate
    :returns: mapping of line number to issue messages
    """
    def _evaluate_file(self, file: str) -> None:
        result = subprocess.run(["java", "-jar", "checkstyle-10.7.0-all.jar", "-c", "sun_checks.xml", "Othello.java"])
        


"""
import os

import subprocess
test = subprocess.run(["java", "-jar", "checkstyle-10.7.0-all.jar", "-c", "sun_checks.xml", "Othello.java"])
print(test)
"""