class RentalDescriptor:
    """Дескриптор для создания свойста(property) у объектов класса Rentable"""
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


    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
