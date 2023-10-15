from battery.battery import Battery
from utils import add_years_to_date

class SpindlerBattery(Battery):
    def __int__(self,last_service_date, current_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_when_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        return date_when_should_be_serviced_by < self.current_date  # Simplified the logic


