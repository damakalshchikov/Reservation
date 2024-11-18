from exceptions.rentable_exceptions import TypeNameRentalError, TypeAddressRentalError, TypePriceError, ValuePriceError, \
    TypeCapacityError, ValueCapacityError


class RentalDescriptor:
    """Дескриптор для создания свойста(property) у объектов класса Rentable"""
    MIN_PRICE: float = 1
    MAX_PRICE: float = float("inf")

    @staticmethod
    def valudate_name(name: str) -> None:
        """Фу-ия валидации названия арендуемого объекта"""

        if not isinstance(name, str):
            raise TypeNameRentalError

    @staticmethod
    def validate_address(address: str) -> None:
        """Фу-ия валидации адреса арендуемого объекта"""

        if not isinstance(address, str):
            raise TypeAddressRentalError

    def validate_price(self, price: int | float) -> None:
        """Фу-ия валидации цены за ночь арендуемого объекта"""

        if not isinstance(price, (int,float)):
            raise TypePriceError
        elif not self.MIN_PRICE <= price <= self.MAX_PRICE:
            raise ValuePriceError(price, self.MIN_PRICE, self.MAX_PRICE)

    @staticmethod
    def validate_capaciry(capacity: int) -> None:
        """Фу-ия валидации вместимости арендуемого объекта"""

        if not isinstance(capacity, int):
            raise TypeCapacityError
        elif capacity <= 0:
            raise ValueCapacityError

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        match self.name:
            case "_name":
                self.valudate_name(value)
            case "_address":
                self.validate_address(value)
            case "_price_per_night":
                self.validate_price(value)
            case "_capacity":
                self.validate_capaciry(value)

        instance.__dict__[self.name] = value
