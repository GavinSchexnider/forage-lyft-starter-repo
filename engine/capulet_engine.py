from engine import Engine

class Capulet_Engine(Engine):
    def __init__(self,last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
    
    def needs_service(self) -> bool:
        time_since_last_service_date = self.current_mileage -self.last_service_mileage
        if time_since_last_service_date >= 30000:
            return True
        else:
            return False