import unittest
from datetime import datetime, timedelta
from unittest.mock import patch  # Ensure patch is imported
from battery import NubbinBattery, SpindlerBattery




class TestNubbinBattery(unittest.TestCase):
    @patch('datetime.datetime')
    def test_needs_service_true(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2022, 1, 1)
        last_service_date = datetime(2017, 1, 1)  # 5 years ago
        current_date = datetime.now()
        battery = NubbinBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())



    def test_needs_service_false(self):
        last_service_date = datetime.now() - timedelta(days=365 * 2)  # 2 years ago
        current_date = datetime.now()
        battery = NubbinBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    @patch('datetime.datetime')
    def test_needs_service_true(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2022, 1, 1)
        last_service_date = datetime(2017, 1, 1)  # 5 years ago
        current_date = datetime.now()
        battery = SpindlerBattery(last_service_date, current_date)

        self.assertTrue(battery.needs_service())
    ...


    def test_needs_service_false(self):
        last_service_date = datetime.now() - timedelta(days=365 * 2)  # 2 years ago
        current_date = datetime.now()
        battery = SpindlerBattery(last_service_date, current_date)

        self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
