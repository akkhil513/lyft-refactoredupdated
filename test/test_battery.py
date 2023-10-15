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
    def test_needs_service_true(self):
        # Case where the battery should need service (last serviced over 3 years ago)
        last_service_date = datetime.now() - timedelta(days=3 * 365 + 1)  # a bit more than 3 years
        battery = SpindlerBattery(last_service_date)
        self.assertTrue(battery.needs_service(), "Battery should need service")

    def test_needs_service_false(self):
        # Case where the battery should not need service (last serviced less than 3 years ago)
        last_service_date = datetime.now() - timedelta(days=3 * 365 - 1)  # a bit less than 3 years
        battery = SpindlerBattery(last_service_date)
        self.assertFalse(battery.needs_service(), "Battery should not need service")
    # @patch('datetime.datetime')
    # def test_needs_service_true(self, mock_datetime):
    #     mock_datetime.now.return_value = datetime(2022, 1, 1)
    #     last_service_date = datetime(2017, 1, 1)  # 5 years ago
    #     current_date = datetime.now()
    #     battery = SpindlerBattery(last_service_date, current_date)
    #
    #     self.assertTrue(battery.needs_service())



    # def test_needs_service_false(self):
    #     last_service_date = datetime.now() - timedelta(days=365 * 2)  # 2 years ago
    #     current_date = datetime.now()
    #     battery = SpindlerBattery(last_service_date, current_date)
    #
    #     self.assertFalse(battery.needs_service())


if __name__ == '__main__':
    unittest.main()
