class TenantNameError(Exception):
    """Исключение имени и(или) фамилии арендатора"""

    def __str__(self) -> str:
        return (
            f"Некорректное имя и(или) фамилия."
            f"Имя и фамилия должны начинаться с заглавной буквы и не сождеражть цифр"
        )


class ValueAgeError(Exception):
    """Исключение недопустимого значения возраста"""

    def __init__(self, age: int, min_age: int, max_age: int):
        self.age: int = age
        self.min_age: int = min_age
        self.max_age: int = max_age

    def __str__(self) -> str:
        return f"Недопустимое значение: {self.age}. Возраст должен быть от {self.min_age} до {self.max_age}"


class TypeAgeError(Exception):
    """Исключение неправильного типа возраста"""

    def __str__(self) -> str:
        return "Возраст должен быть целым числом"


class PhoneNumberError(Exception):
    """Исключение некорректного номера телефона"""

    def __str__(self) -> str:
        return "Некорректный номер телефона. Должен начинаться с 89 или +79 и содержать 11 цифр"
