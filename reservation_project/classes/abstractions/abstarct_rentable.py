from abc import ABC, abstractmethod


class Rentable(ABC):
    """Абстрактный класс, который представляет собой арендуемый объект"""

    def __init__(self, rental_id: int, name: str, address: str, price_per_night: float, capacity: int) -> None:
        self._rental_id: int = rental_id
        self._name: str = name
        self._address: str = address
        self._price_per_night: float = price_per_night
        self._capacity: int = capacity
        self._available_capacity: int = capacity

    def to_dict(self) -> dict:
        """Возвращает словарь с данными арендуемого объекта"""
        return {
            "rental_id": self._rental_id,
            "name": self._name,
            "address": self._address,
            "price_per_night": self._price_per_night,
            "capacity": self._capacity,
            "available_capacity": self._available_capacity,
        }

    @staticmethod
    @abstractmethod
    def from_dict(data: dict) -> "Rentable":
        """Создаёт объект Rentable из словаря"""
        pass

    def is_fully_booked(self) -> bool:
        """Проверяет на наличие свободных мест"""
        return self._available_capacity == 0