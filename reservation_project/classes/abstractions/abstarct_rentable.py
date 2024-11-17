from abc import ABC, abstractmethod


class Rentable(ABC):
    """Абстрактный класс, который представляет собой арендуемый объект"""

    def __init__(self, rental_id: int, name: str, address: str, price_per_night: float, capacity: int) -> None:
        self._rental_id: int = rental_id
        self.name: str = name
        self.address: str = address
        self.price_per_night: float = price_per_night
        self.capacity: int = capacity
        self.available_capacity: int = capacity

    def to_dict(self) -> dict:
        """Возвращает словарь с данными арендуемого объекта"""
        return {
            "rental_id": self._rental_id,
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