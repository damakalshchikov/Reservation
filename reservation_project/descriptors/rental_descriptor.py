class RentalDescriptor:
    """Дескриптор для создания свойста(property) у объектов класса Rentable"""
    @staticmethod
    def valudate_name(name: str) -> None:
        """Фу-ия валидации названия аврендуемого объекта"""

        if not isinstance(name, str):
            raise TypeNameRentalError


    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
