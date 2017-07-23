import unittest

from .base_test import BaseTestCase


@unittest.skip("We can't get the connection through a different port to work.")
class TestBasicProxy(BaseTestCase, unittest.TestCase):
    url = "http://localhost:8005"
