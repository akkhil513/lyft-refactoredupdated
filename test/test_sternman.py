import unittest
from datetime import timedelta, datetime

from engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced_when_warning_light_is_on(self):
        last_service_date = datetime.now() - timedelta(days=365)
        engine = SternmanEngine(last_service_date, True)
        self.assertTrue(engine.engine_should_be_serviced())

    def test_should_not_be_serviced_when_warning_light_is_off(self):
        last_service_date = datetime.now() - timedelta(days=365)
        engine = SternmanEngine(last_service_date, False)
        self.assertFalse(engine.engine_should_be_serviced())
