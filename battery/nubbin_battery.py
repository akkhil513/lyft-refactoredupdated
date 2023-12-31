from battery.battery import Battery
from utils import add_years_to_date

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date

    def needs_service(self):
        date_when_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        return date_when_should_be_serviced_by < self.current_date


