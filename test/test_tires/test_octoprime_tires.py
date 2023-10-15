import unittest
from datetime import datetime, timedelta

from tires.octoprime_tire import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):

    def test_tires_need_service_due_to_age(self):
        old_date = datetime.now() - timedelta(days=2200)  # About 6 years
        tire = OctoprimeTires(30, old_date, [0.5, 0.5, 0.5, 0.5])  # Added wear_values
        self.assertTrue(tire.tires_need_service())

    def test_tires_need_service_due_to_low_pressure(self):
        current_date = datetime.now()
        tire = OctoprimeTires(27, current_date, [0.5, 0.5, 0.5, 0.5])  # Added wear_values
        self.assertTrue(tire.tires_need_service())

    def test_tires_do_not_need_service(self):
        current_date = datetime.now()
        tire = OctoprimeTires(30, current_date, [0.5, 0.5, 0.5, 0.5])  # Added wear_values
        self.assertFalse(tire.tires_need_service())

    def test_octoprime_tires_service(self):
        # Octoprime tires should be serviced if the sum of wear values is 3 or more.
        self.assertTrue(OctoprimeTires(30, datetime.now(), [0.8, 0.8, 0.8, 0.8]).tires_need_service())
        self.assertFalse(OctoprimeTires(30, datetime.now(), [0.7, 0.7, 0.7, 0.7]).tires_need_service())
