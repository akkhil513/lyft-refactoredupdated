class Battery:
    def __init__(self, last_service_date=None):
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        """
        Determine whether the battery needs to be serviced.
        This method should be overridden by subclasses with specific logic.
        """
        pass