from classes.abstractions.abstarct_rentable import Rentable
from descriptors.tenant_descriptor import TenantDescriptor


class Tenant:
    """Класс, представляющий арендатора"""

    _next_id: int = 1

    first_name: TenantDescriptor = TenantDescriptor()
    last_name: TenantDescriptor = TenantDescriptor()
    age: TenantDescriptor = TenantDescriptor()
    money: TenantDescriptor = TenantDescriptor()
    phone_number: TenantDescriptor = TenantDescriptor()

    def __init__(self, first_name: str, last_name: str, age: int, money: int | float, phone_number: str):
        self._id: int = Tenant._next_id
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.age: int = age
        self.money: int| float = money
        self.phone_number: str = phone_number
        self._place_of_residence: None | Rentable = None
        Tenant._next_id += 1

    def __str__(self):
        return f"Арендатор:\nИмя: {self.first_name}\nФамилия: {self.last_name}\nБюджет: {self.money}"

    @property
    def tenant_id(self) -> int:
        return self._id

    def to_dict(self) -> dict:
        """Возвращает словарь с данными арендатора"""

        return {
            "id": self._id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "money": self.money,
            "phone_number": self.phone_number,
            "place_of_residence": self._place_of_residence.to_dict() if self._place_of_residence else None,
        }

    @staticmethod
    def from_dict(data: dict) -> "Tenant":
        """Создаёт объект Tenant из словаря"""

        tenant = Tenant(
            first_name=data["first_name"],
            last_name=data["last_name"],
            age=data["age"],
            money=data["money"],
            phone_number=data["phone_number"],
        )

        return tenant

    def attach_rental(self, rentable: Rentable) -> None:
        """Привязывает арендатора к месту проживания"""

        self._place_of_residence = rentable

    def detach_rental(self) -> None:
        """Отвязывает арендатора от места проживания"""

        self._place_of_residence = None

    def has_rental(self) -> bool:
        """Проверяет, проживает ли арендатор в арендуемом жилье"""

        return self._place_of_residence is not None
