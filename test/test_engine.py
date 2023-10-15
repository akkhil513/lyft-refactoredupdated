import unittest
from datetime import datetime, timedelta
from unittest import TestCase
from engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(TestCase):

    def test_capulet_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30000

        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced_when_warning_light_is_on(self):
        last_service_date = datetime.now() - timedelta(days=365)
        engine = SternmanEngine(last_service_date, True)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_should_not_be_serviced_when_warning_light_is_off(self):
        last_service_date = datetime.now() - timedelta(days=365)
        engine = SternmanEngine(last_service_date, False)
        self.assertFalse(engine.engine_should_be_serviced())


class TestWilloughby(unittest.TestCase):
    def testNeedsService(self):
        last_service_mileage = 0
        current_mileage = 60001
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.engine_should_be_serviced())

    def testDoesNotNeedService(self):
        last_service_mileage = 0
        current_mileage = 60000
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
