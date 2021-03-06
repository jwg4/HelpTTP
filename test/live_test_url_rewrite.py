import unittest

import requests

from .base_test import BaseTestCase


class TestBasicProxy(BaseTestCase, unittest.TestCase):
    url = "http://localhost:80/"
    internal_url = "http://localhost:5555/foo"

    def test_can_retrieve_url(self):
        url = self.internal_url + "/json"
        r = requests.get(url)
        data = r.json()
        self.assertIn('address', data)
        self.assertIn('url', data['address'])
        self.assertEqual(data['address']['url'], url)

