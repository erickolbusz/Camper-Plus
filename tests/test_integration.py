"""Integration Tests for Camper+ App"""

import unittest
import camperapp
from camperapp.models import db, CampEvent, CampGroup, Camper
import json
from datetime import datetime


class TestUrls(unittest.TestCase):
    def setUp(self):
        self.app = camperapp.app.test_client()
        self.app.application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.app = self.app.application
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home(self):
        """Test that home can be accessed"""
        response = self.app.get("/")
        self.assertTrue(response.status_code, 200)

    def test_calendar(self):
        """Test that the Calendar Page can be accessed"""
        response = self.app.get("/schedule")
        self.assertTrue(response.status_code, 200)

    def test_campers(self):
        """Test that the Calendar Page can be accessed"""
        response = self.app.get("/campers")
        self.assertTrue(response.status_code, 200)

    def test_post_event_on_schedule_page(self):
        """Test that roups passed to the schedule page are all displayed"""
        json_data = {
            'title': 'Test Event',
            'start': '2017-8-8T12:00:00',
            'end': '2017-8-8T12:00:00',
            'group': '3'
        }

        response = self.app.post("/saveEvent", data=json.dumps(json_data),
                    content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_put_event_on_schedule_page(self):
        """Test that roups passed to the schedule page are all displayed"""
        json_data = {
            'title': 'Test Event',
            'start': '2017-8-8T12:00:00',
            'end': '2017-8-8T12:00:00',
            'group': '3'
        }

        response = self.app.put("/saveEvent", data=json.dumps(json_data),
                    content_type='application/json')
        self.assertTrue(response.status_code, 200)

    def test_get_calendar_events_endpoint(self):
        event = CampEvent('Basketball', datetime.now(), datetime.now())
        group = CampGroup('falcons', 'green')
        group.events.append(event)
        db.session.add(group)
        db.session.add(event)
        db.session.commit()

        response = self.app.get('/getCampEvents?start=2013-12-01&end=2014-01-12')
        self.assertTrue(response.status_code, 200)
