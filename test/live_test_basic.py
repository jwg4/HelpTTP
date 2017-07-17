import unittest

import requests


class TestBasicProxy(unittest.TestCase):
    def test_can_retrieve(self):
        r = requests.get("http://localhost:80/")
        self.assertEqual(r.status_code, 200)