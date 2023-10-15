class Engine:
    def __init__(self, last_service_date=None):
        self.last_service_date = last_service_date

    def engine_should_be_serviced(self):
        """
        Determine whether the engine needs to be serviced.
        This method should be overridden by subclasses with specific logic.
        """
        raise NotImplementedError("This method should be overridden by subclass")


