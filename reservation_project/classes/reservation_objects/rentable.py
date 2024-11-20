from classes.abstractions.abstarct_rentable import Rentable


class Room(Rentable):
    """Класс, который представляет комнату для аренды"""

    def __init__(self, name: str, address: str, price_per_night: int | float):
        super().__init__(name, address, price_per_night, capacity=2)

    @staticmethod
    def from_dict(data: dict) -> "Room":
        return Room(
            name=data["name"],
            address=data["address"],
            price_per_night=data["price_per_night"]
        )


class Apartment(Rentable):
    """Класс, который представляет квартиру для аренды"""

    def __init__(self, name: str, address: str, price_per_night: int | float):
        super().__init__(name, address, price_per_night, capacity=4)

    @staticmethod
    def from_dict(data: dict) -> "Apartment":
        return Apartment(
            name=data["name"],
            address=data["address"],
            price_per_night=data["price_per_night"]
        )


class House(Rentable):
    """Класс, который представляет дом для аренды"""

    def __init__(self, name: str, address: str, price_per_night: int | float):
        super().__init__(name, address, price_per_night, capacity=8)

    @staticmethod
    def from_dict(data: dict) -> "House":
        return House(
            name=data["name"],
            address=data["address"],
            price_per_night=data["price_per_night"]
        )
