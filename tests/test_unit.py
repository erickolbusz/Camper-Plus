"""Unit Tests for Camper+ App"""

import unittest
import camperapp
from camperapp.models import CampEvent
import mock
from unittest.mock import patch, DEFAULT, create_autospec
from datetime import datetime


class TestApp(unittest.TestCase):

    def test_schedule_gets_schedule_template(self):
        """Test that the Schedule endpoint calls the schedule Page"""
        with patch.multiple('camperapp.routes', render_template=DEFAULT) as \
                mock_funcs:
            camperapp.routes.schedule()
            render_template = mock_funcs['render_template']
            self.assertTrue(render_template.called)
            call_args = render_template.call_args
            template_name = call_args[0][0]
            self.assertEqual(template_name, "schedule.html")

    def test_campers_gets_campers_template(self):
        """Test that the Schedule endpoint calls the schedule Page"""
        with patch.multiple('camperapp.routes', render_template=DEFAULT) as \
                mock_funcs:
            camperapp.routes.campers()
            render_template = mock_funcs['render_template']
            self.assertTrue(render_template.called)
            call_args = render_template.call_args
            template_name = call_args[0][0]
            self.assertEqual(template_name, "campers.html")

    def test_login_gets_login_template(self):
        """Test that the login route exists"""
        with patch.multiple("camperapp.routes", render_template=DEFAULT) as \
                mock_functions:
            camperapp.routes.login()
            render_template = mock_functions["render_template"]
            self.assertTrue(render_template.called)
            call_args = render_template.call_args
            file_name = call_args[0][0]
            self.assertEqual(file_name, "login.html")

    @mock.patch('camperapp.models.datetime')
    def test_CampEvent_convert_ISO_py_datetime(self, mock_datetime):
        ISO_datetime = "2017-10-10T12:25:27"
        self.assertTrue(camperapp.models.datetime is mock_datetime)
        CampEvent.convert_ISO_datetime_to_py_datetime(CampEvent, ISO_datetime)
        mock_datetime.strptime.assert_called_once_with(ISO_datetime, '%Y-%m-%dT%H:%M:%S')
