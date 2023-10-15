from tires import Tires
from datetime import datetime , timedelta

class GoodYearTires(Tires):
    MIN_PRESSURE = 30
    MAX_PRESSURE = 35
    MAX_AGE = 5 #years

    def __init__(self, current_pressure, manufacture_date):
        self.current_pressure = current_pressure
        self.manufacture_date = manufacture_date

    def _is_pressure_out_of_limits(self):
        is_below_min_pressure = self.current_pressure < self.MIN_PRESSURE
        is_above_max_pressure = self.current_pressure > self.MAX_PRESSURE

        return is_above_max_pressure or is_below_min_pressure

    def _is_too_old(self):
        age = (datetime.now() - self.manufacture_date)
        max_age_days = self.MAX_AGE * 365  # Convert max age to days
        return age.days > max_age_days

    def tires_need_service(self):
        return self._is_pressure_out_of_limits() or self._is_too_old()



