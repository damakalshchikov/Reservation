class TypeNameRentalError(Exception):
    """Исключение неверного типа названия арендуемого объекта"""

    def __str__(self) -> str:
        return "Название арендуемого объекта должно быть строкой"


class TypeAddressRentalError(Exception):
    """Исключение неверного типа адреса арендуемого объекта"""

    def __str__(self) -> str:
        return "Адрес должен быть строковым значением"


class FullReservationError(Exception):
    """Исключение о переполнении арендуемого объекта"""

    def __init__(self, rental_name: str):
        self.rental_name: str = rental_name

    def __str__(self) -> str:
        return f"""Арендуемый объект "{self.rental_name}" переполнен"""