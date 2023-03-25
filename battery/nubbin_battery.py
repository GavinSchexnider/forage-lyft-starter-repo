from battery import Battery

class Nubbin_Battery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        time_since_last_service_date = self.current_date - self.last_service_date
        if time_since_last_service_date >= 3:
            return True
        else:
            return False