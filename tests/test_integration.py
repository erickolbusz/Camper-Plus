"""Integration Tests for Camper+ App"""

import unittest
import camperapp
from bs4 import BeautifulSoup


class TestCamperAppInt(unittest.TestCase):

    def setUp(self):
        self.app = camperapp.app.test_client()

    def test_one(self):
        self.assertTrue(True)
