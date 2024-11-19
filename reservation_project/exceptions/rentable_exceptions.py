class TypeNameRentalError(Exception):
    """Исключение неверного типа названия арендуемого объекта"""

    def __str__(self) -> str:
        return "Название арендуемого объекта должно быть строкой"


class TypeAddressRentalError(Exception):
    """Исключение неверного типа адреса арендуемого объекта"""

    def __str__(self) -> str:
        return "Адрес должен быть строковым значением"


class TypePriceError(Exception):
    """Исключение о неверном типе цены за ночь арендуемого объекта"""

    def __str__(self) -> str:
        return "Цена за ночь должна быть целым/дробным числом"


class ValuePriceError(Exception):
    """Исключение о неверном значении цены за ночь арендуемого объекта"""

    def __init__(self, price: float, min_price: float, max_price: float):
        self.price: float = price
        self.min_price: float = min_price
        self.max_price: float = max_price

    def __str__(self) -> str:
        return f"Недопустимое значение цены: {self.price}. Цена должна быть в диапазоне от {self.min_price} до {self.max_price}"
