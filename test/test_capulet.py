from unittest import TestCase

from engine.capulet_engine import CapuletEngine


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