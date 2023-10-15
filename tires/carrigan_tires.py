import self

from tires import Tires
from datetime import datetime , timedelta

class CarriganTires(Tires):
    MIN_PRESSURE = 30
    MAX_PRESSURE = 35
    MAX_AGE = 5 #years

    def __init__(self, current_pressure, manufacture_date,wear_values):
        self.wear_values = wear_values
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

    def _needs_service_due_to_wear(self):
        return any(wear >= 0.9 for wear in self.wear_values)

    # def tires_need_service(self):
    #     return self._is_pressure_out_of_limits() or self._is_too_old() or self._is_worn_out()
    def tires_need_service(self):
        return (self._is_pressure_out_of_limits() or self._is_too_old() or self._needs_service_due_to_wear())





