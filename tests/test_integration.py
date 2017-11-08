"""Integration Tests for Camper+ App"""

import unittest
import camperapp
from bs4 import BeautifulSoup


class TestCamperAppInt(unittest.TestCase):

    def setUp(self):
        self.app = camperapp.app.test_client()

    def test_schedule_calendar(self):

        rv = self.app.get('/schedule')
        soup = BeautifulSoup(rv.data, 'html.parser')
        schedule = soup.find('div', {'class': 'sched-div'})
        self.assertTrue('calender' == schedule.get('id'))
