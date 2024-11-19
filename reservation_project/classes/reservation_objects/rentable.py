from classes.abstractions.abstarct_rentable import Rentable


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
