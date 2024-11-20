from abc import ABC, abstractmethod

from descriptors.rental_descriptor import RentalDescriptor


class Rentable(ABC):
    """Абстрактный класс, который представляет собой арендуемый объект"""

    _next_id: int = 1

    name: RentalDescriptor = RentalDescriptor()
    address: RentalDescriptor = RentalDescriptor()
    price_per_night: RentalDescriptor = RentalDescriptor()

    def __init__(self, name: str, address: str, price_per_night: float, capacity: int):
        self._id: int = Rentable._next_id
        self.name: str = name
        self.address: str = address
        self.price_per_night: int | float = price_per_night
        self.__capacity: int = capacity
        self.__available_capacity: int = capacity
        Rentable._next_id += 1

    @property
    def rentable_id(self) -> int:
        return self._id

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
        }

    @staticmethod
    @abstractmethod
    def from_dict(data: dict) -> "Rentable":
        """Создаёт объект Rentable из словаря"""

        pass

    def is_fully_booked(self) -> bool:
        """Проверяет на наличие свободных мест"""

        return self.available_capacity == 0
