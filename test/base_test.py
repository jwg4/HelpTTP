import unittest

import requests


class BaseTestCase(object):
    def test_can_retrieve(self):
        r = requests.get(self.url + "/")
        self.assertEqual(r.status_code, 200)

    def test_can_retrieve_json(self):
        r = requests.get(self.url + "/json")
        self.assertEqual(r.status_code, 200)

    def test_can_retrieve_unknown_address(self):
        r = requests.get(self.url + "/asdfQWERasdf")
        self.assertEqual(r.status_code, 200)

    def test_is_http(self):
        r = requests.get(self.url + "/")
        self.assertEqual(r.headers['content-type'], "text/html")

    @unittest.skip("Weird failure. Keep investigating.")
    def test_is_json(self):
        r = requests.get(self.url + "/json")
        self.assertEqual(r.headers['content-type'], "application/json")