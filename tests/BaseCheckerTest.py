import requests
import json
import unittest
import os

class BaseCheckerTest(unittest.TestCase):
    PROGRAMS_PATH = "tests/sample_programs/"
    TEST_FILE_PATH = os.getcwd() + "/temp.java"
    API_URL = "http://127.0.0.1:8000"

    def base_test_check_success(self, path: str, messages: list):
        with open(f"{self.PROGRAMS_PATH}/{path}") as f:
            actual = json.loads(requests.post(self.API_URL, json.dumps({
                "text": f.read()
            })).text)
        
        expected = {
            "messages": messages
        }
        self.assertEqual(actual, expected)