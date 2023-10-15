from datetime import datetime

from battery.battery import Battery
from utils import add_years_to_date
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date=None):
        self.last_service_date = last_service_date
        self.current_date = current_date if current_date is not None else datetime.now()

    def needs_service(self):
        date_when_should_be_serviced_by = add_years_to_date(self.last_service_date, 3)
        return date_when_should_be_serviced_by < self.current_date

    # def needs_service(self):
    #     age_of_battery = self.current_date - self.last_service_date
    #     # Check if the age of the battery is more than 3 years
    #     return age_of_battery > timedelta(days=3 * 365)
