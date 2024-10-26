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


class USCar(Car):
    def __init__(self, make: str, model: str):
        super().__init__(make, model)
        self.spec = "US"

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.spec} spec): Двигун запущено")


class EUCar(Car):
    def __init__(self, make: str, model: str):
        super().__init__(make, model)
        self.spec = "EU"

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.spec} spec): Двигун запущено")


class USMotorcycle(Motorcycle):
    def __init__(self, make: str, model: str):
        super().__init__(make, model)
        self.spec = "US"

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.spec} spec): Мотор заведено")


class EUMotorcycle(Motorcycle):
    def __init__(self, make: str, model: str):
        super().__init__(make, model)
        self.spec = "EU"

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.spec} spec): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> USCar:
        return USCar(make, model)

    def create_motorcycle(self, make: str, model: str) -> USMotorcycle:
        return USMotorcycle(make, model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> EUCar:
        return EUCar(make, model)

    def create_motorcycle(self, make: str, model: str) -> EUMotorcycle:
        return EUMotorcycle(make, model)


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
