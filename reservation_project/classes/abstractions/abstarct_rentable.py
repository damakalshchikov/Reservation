from abc import ABC, abstractmethod

from descriptors.rental_descriptor import RentalDescriptor


class Rentable(ABC):
    """Абстрактный класс, который представляет собой арендуемый объект"""

    name: RentalDescriptor = RentalDescriptor()
    address: RentalDescriptor = RentalDescriptor()
    price_per_night: RentalDescriptor = RentalDescriptor()

    def __init__(self, name: str, address: str, price_per_night: float, capacity: int):
        self.name: str = name
        self.address: str = address
        self.price_per_night: int | float = price_per_night
        self.__capacity: int = capacity
        self.__available_capacity: int = capacity

    @property
    def capacity(self) -> int:
        return self.__capacity

    @property
    def available_capacity(self) -> int:
        return self.__available_capacity

    @available_capacity.setter
    def available_capacity(self, available_capacity: int) -> None:
        self.__available_capacity: int = available_capacity

    def to_dict(self) -> dict:
        """Возвращает словарь с данными арендуемого объекта"""

        return {
            "name": self.name,
            "address": self.address,
            "price_per_night": self.price_per_night,
            "capacity": self.capacity,
            "available_capacity": self.available_capacity,
        }

    @staticmethod
    @abstractmethod
    def from_dict(data: dict) -> "Rentable":
        """Создаёт объект Rentable из словаря"""

        pass

    def is_fully_booked(self) -> bool:
        """Проверяет на наличие свободных мест"""

        return self.available_capacity == 0
