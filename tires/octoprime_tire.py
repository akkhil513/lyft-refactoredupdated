#from tires.tires import Tires
from datetime import datetime, timedelta
from tires import Tires


class OctoprimeTires(Tires):
    MIN_PRESSURE: float = 28.0
    MAX_PRESSURE: float = 33.0
    MAX_AGE: int = 6  # years

    def __init__(self, current_pressure, manufacture_date,wear_values):
        self.wear_values = wear_values
        self.current_pressure = current_pressure
        self.manufacture_date = manufacture_date

    def _is_pressure_out_of_limits(self):
        is_below_min_pressure = self.current_pressure < self.MIN_PRESSURE
        is_above_max_pressure = self.current_pressure > self.MAX_PRESSURE
        return is_above_max_pressure or is_below_min_pressure

    def _is_too_old(self):
        age = (datetime.now() - self.manufacture_date).days
        max_age_days = self.MAX_AGE * 365  # Convert max age to days
        return age > max_age_days

    def _is_worn_out(self):
        return sum(self.wear_values) >= 3

    def tires_need_service(self):
        return self._is_pressure_out_of_limits() or self._is_too_old() or self._is_worn_out()
