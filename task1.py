from abc import abstractmethod, ABC
import logging

logging.basicConfig(
    format="%(levelname)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def __init__(self):
        self.spec = "(US Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} {self.spec}")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} {self.spec}")


class EUVehicleFactory(VehicleFactory):
    def __init__(self):
        self.spec = "(EU Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, f"{model} {self.spec}")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, f"{model} {self.spec}")


# Використання

usFactory = USVehicleFactory()

vehicle1 = usFactory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = usFactory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()

euFactory = EUVehicleFactory()

vehicle1 = euFactory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = euFactory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
