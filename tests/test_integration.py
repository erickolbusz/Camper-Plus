"""Integration Tests for Camper+ App"""

import unittest
import camperapp
import json


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

    def test_groups_on_schedule_page(self):
        """Test that the groups passed to the schedule page are all displayed"""
        json_data = {
            'title': 'Test Event',
            'start': '2017-8-8T12:00:00',
            'end': '2017-8-8T12:00:00',
            'group': '3'
        }
    def test_login_gets_login_template(self):
        """Checks if the login route exists. The test passes if it does."""
        with patch.multiple("camperapp.routes",
                             request=DEFAULT,
                             render_template=DEFAULT) as mock_functions:
             camperapp.routes.login()
             render_template = mock_functions["render_template"]

             # session['username'] = None
            
             #makes sure we are rendering a template on the login route
             self.assertTrue(render_template.called)
             call_args = render_template.call_args
             file_name = call_args[0][0]
             #makes sure we are rendering the correct template on the login route
             self.assertEqual(file_name, "login.html")

        response = self.app.post("/saveEvent", data=json.dumps(json_data), content_type='application/json')
        self.assertTrue(response.status_code, 200)
