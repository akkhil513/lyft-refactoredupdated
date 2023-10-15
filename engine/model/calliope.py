from datetime import datetime, timedelta
from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def engine_should_be_serviced(self) -> bool:
        service_threshold_date = self.last_service_date + timedelta(days=365 * 2)  # 2 years
        print(f"Service Threshold Date: {service_threshold_date}")
        engine_health_ok = self.check_engine_health()
        return service_threshold_date < datetime.today().date() or not engine_health_ok

    def check_engine_health(self) -> bool:
        # Implement a method to check the health of the engine and return a boolean
        pass

    def needs_service(self):
        pass
