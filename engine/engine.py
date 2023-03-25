import abstractmethod

class Engine:


    @abstractmethod
    def needs_service() -> bool:
        pass