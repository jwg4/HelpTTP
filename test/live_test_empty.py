import unittest

from .base_test import BaseTestCase


class TestNoProxy(BaseTestCase, unittest.TestCase):
    url = "http://localhost:5555"
