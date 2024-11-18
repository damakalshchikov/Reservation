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


    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
