from abc import ABC, abstractmethod

class Check(ABC):
    """
    Check TODO
    """
    def __init__(self, message: str):
        self.message: str = message

    """
    Evaluate a line

    :param line: line to evaluate
    :returns: true if line is valid
    """
    @abstractmethod
    def evaluate_line(self, line: str) -> bool:
        pass
