import unittest
from datetime import datetime, timedelta
from tires.goodyear_tire import GoodYearTires  # Update this import based on your file structure


class TestGoodYearTires(unittest.TestCase):

    def test_tires_need_service_due_to_low_pressure(self):
        current_date = datetime.now()
        tire = GoodYearTires(25, current_date)  # Below MIN_PRESSURE
        result = tire.tires_need_service()
        print(f"Tire needs service: {result}")
        self.assertTrue(tire.tires_need_service(), "Failed: Low pressure should require service")

    def test_tires_need_service_due_to_high_pressure(self):
        current_date = datetime.now()
        tire = GoodYearTires(40, current_date)  # Above MAX_PRESSURE
        result = tire.tires_need_service()
        print(f"Tire needs service: {result}")
        self.assertTrue(tire.tires_need_service(), "Failed: High pressure should require service")

    def test_tires_need_service_due_to_old_age(self):
        old_date = datetime.now() - timedelta(days=2000)  # More than 5 years
        tire = GoodYearTires(32, old_date)
        result = tire.tires_need_service()
        print(f"\nTest 'test_tires_need_service_due_to_old_age': Tire needs service: {result}")
        self.assertTrue(tire.tires_need_service(), "Failed: Old age should require service")

    def test_tires_do_not_need_service(self):
        current_date = datetime.now()
        tire = GoodYearTires(32, current_date)
        result = tire.tires_need_service()
        print(f"\nTest 'test_tires_need_service_due_to_old_age': Tire needs service: {result}")
        self.assertFalse(tire.tires_need_service(), "Failed: Tire should not require service")


if __name__ == "__main__":
    unittest.main()
