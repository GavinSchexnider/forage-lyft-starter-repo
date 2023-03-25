import abstractmethod
from car import Car

class CarFactory():


    @abstractmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        pass

    @abstractmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        pass

    @abstractmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_lght_on: bool) -> Car:
        pass

    @abstractmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        pass

    @abstractmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        pass