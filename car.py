from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, battery, engine):
        self.battery = battery
        self.engine = engine

    
    def needs_service(self):
        does_battery_need_service: bool = self.battery.needs_service()
        does_engine_need_service: bool = self.engine.needs_service()
        if does_battery_need_service or does_engine_need_service:
            return True
        else:
            return False