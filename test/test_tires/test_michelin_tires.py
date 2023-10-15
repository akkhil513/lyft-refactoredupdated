import unittest
from datetime import datetime, timedelta

from tires.michelin_tire import MichelinTires


class TestMichelinTires(unittest.TestCase):

    def test_tires_need_service_due_to_age(self):
        old_date = datetime.now() - timedelta(days=2200)  # About 6 years
        tire = MichelinTires(30, old_date)
        self.assertTrue(tire.tires_need_service())

    def test_tires_need_service_due_to_low_pressure(self):
        current_date = datetime.now()
        tire = MichelinTires(27, current_date)  # Below MIN_PRESSURE
        self.assertTrue(tire.tires_need_service())

    def test_tires_do_not_need_service(self):
        current_date = datetime.now()
        tire = MichelinTires(30, current_date)
        self.assertFalse(tire.tires_need_service())

if __name__ == "__main__":
    unittest.main()
