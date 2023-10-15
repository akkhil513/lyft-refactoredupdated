import unittest
from datetime import datetime, timedelta
from tires.carrigan_tires import CarriganTires  # Update based on your file structure


class TestCarriganTires(unittest.TestCase):

    def test_tires_need_service_due_to_low_pressure(self):
        current_date = datetime.now()
        tire = CarriganTires(25, current_date, [0.5, 0.5, 0.5, 0.5])  # Added wear_values
        result = tire.tires_need_service()
        print(f"Tire needs service: {result}")
        self.assertTrue(result, "Failed: Low pressure should require service")

    def test_tires_need_service_due_to_high_pressure(self):
        current_date = datetime.now()
        tire = CarriganTires(40, current_date, [0.5, 0.5, 0.5, 0.5])  # Added wear_values
        result = tire.tires_need_service()
        print(f"Tire needs service: {result}")
        self.assertTrue(result, "Failed: High pressure should require service")

    def test_tires_need_service_due_to_old_age(self):
        old_date = datetime.now() - timedelta(days=2000)  # More than 5 years
        tire = CarriganTires(32, old_date, [0.5, 0.5, 0.5, 0.5])  # Added wear_values
        result = tire.tires_need_service()
        print(f"\nTest 'test_tires_need_service_due_to_old_age': Tire needs service: {result}")
        self.assertTrue(result, "Failed: Old age should require service")

    def test_tires_do_not_need_service(self):
        current_date = datetime.now()
        tire = CarriganTires(32, current_date, [0.5, 0.5, 0.5, 0.5])  # Added wear_values
        result = tire.tires_need_service()
        print(f"\nTest 'test_tires_do_not_need_service': Tire needs service: {result}")
        self.assertFalse(result, "Failed: Tire should not require service")

    def test_tires_need_service_due_to_wear(self):
        # Carrigan tires should be serviced if any wear value is 0.9 or more.
        self.assertTrue(CarriganTires(30, datetime.now(), [0.8, 0.8, 0.9, 0.8]).tires_need_service())
        self.assertFalse(CarriganTires(30, datetime.now(), [0.8, 0.8, 0.8, 0.8]).tires_need_service())


if __name__ == "__main__":
    unittest.main()
