from classes.abstractions.abstarct_rentable import Rentable


class Apartment(Rentable):
    """Класс, который представляет квартиру для аренды"""

    @staticmethod
    def from_dict(data: dict) -> "Apartment":
        return Apartment(
            name=data["name"],
            address=data["address"],
            price_per_night=data["price_per_night"],
            capacity=data["capacity"],
        )
