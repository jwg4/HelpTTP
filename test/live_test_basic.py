import unittest

import requests


class TestBasicProxy(unittest.TestCase):
    def test_can_retrieve(self):
        r = requests.get("http://localhost:80/")
        self.assertEqual(r.status_code, 200)

    def test_is_http(self):
        r = requests.get("http://localhost:80/")
        self.assertEqual(r.headers['content-type'], "text/html")

    def test_is_json(self):
        r = requests.get("http://localhost:80/json")
        self.assertEqual(r.headers['content-type'], "application/json")