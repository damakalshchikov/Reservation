class TenantNameError(Exception):
    def __str__(self):
        return (
            f"Некорректное имя и(или) фамилия."
            f"Имя и фамилия должны начинаться с заглавной буквы и не сождеражть цифр"
        )

class ValueAgeError(Exception):
    def __init__(self, age: int, min_age: int, max_age: int):
        self.age: int = age
        self.min_age: int = min_age
        self.max_age: int = max_age

    def __str__(self):
        return f"Недопустимое значение: {self.age}. Возраст должен быть от {self.min_age} до {self.max_age}"


class TypeAgeError(Exception):
    def __str__(self):
        return "Возраст должен быть целым числом"


class PhoneNumberError(Exception):
    def __str__(self) -> str:
        return "Некорректный номер телефона. Должен начинаться с 89 или +79 и содержать 11 цифр"


class HaveRentError(Exception):
    def __init__(self, rentable_address: str, tenant_first_name: str, tenant_last_name: str) -> None:
        self.rentable_address: str = rentable_address
        self.tenant_first_name: str = tenant_first_name
        self.tenant_last_name: str = tenant_last_name

    def __str__(self) -> str:
        return f"{self.tenant_first_name} {self.tenant_last_name} уже проживает по адресу: {self.rentable_address}"
