"""Unit Tests for Camper+ App"""

import unittest
import camperapp
from unittest.mock import patch, DEFAULT


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
