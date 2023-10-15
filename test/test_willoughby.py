import unittest
from engine.willoughby_engine import WilloughbyEngine


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




