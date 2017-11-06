"""Integration Tests for Camper+ App"""

import unittest
import camperapp
from bs4 import BeautifulSoup


class TestCamperAppInt(unittest.TestCase):

    def setUp(self):
        self.app = camperapp.app.test_client()

    def test_schedule_calendar(self):
        calendar_url = "https://calendar.google.com/calendar/embed?height=600&amp;wkst=1&amp;bgcolor=%23FFFFFF&amp;\
        src=9dn2cvujfk9rsfnlvdmn2rchg0%40group.calendar.google.com&amp;color=%2323164E&amp;ctz=America%2FNew_York"
        rv = self.app.get('/schedule')
        soup = BeautifulSoup(rv.data, 'html.parser')
        schedule = soup.find('div', {'class': 'sched-div'})
        cal = schedule.find('iframe')
        self.assertEqual(cal.get('src'), calendar_url)
