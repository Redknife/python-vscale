import os
import unittest

DATA_DIR = 'data'


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.end_point = "https://api.vscale.io/v1/"
        self.token = "verysecuritytoken"

    def load_from_file(self, json_file):
        cwd = os.path.dirname(__file__)
        file_abs_path = os.path.join(cwd, '{}/{}'.format(DATA_DIR, json_file))
        with open(file_abs_path, 'r') as f:
            return f.read()
