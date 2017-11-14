"""Integration Tests for Camper+ App"""

import unittest
import camperapp


class TestUrls(unittest.TestCase):
    def setUp(self):
        self.app = camperapp.app.test_client()

    def test_home(self):
        """Test that home can be accessed"""
        response = self.app.get("/")
        self.assertTrue(response.status_code, 200)

    def test_calendar(self):
        """Test that the Calendar Page can be accessed"""
        response = self.app.get("/schedule")
        self.assertTrue(response.status_code, 200)
