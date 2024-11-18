import re

from exceptions.tenant_exceptions import TypeAgeError, ValueAgeError, TenantNameError, PhoneNumberError


class TenantDescriptor:
    # Минимальный и максимальный возрасты для заключения договора
    MIN_AGE: int = 18
    MAX_AGE: int = 99
    FIRST_AND_LAST_NAME_PATTERN: str = r"^[А-я][а-яА-Я]*$"

    def validate_name(self, name: str) -> None:
        if not re.match(self.FIRST_AND_LAST_NAME_PATTERN, name):
            raise TenantNameError

    def validate_age(self, age: int) -> None:
        if not isinstance(age, int):
            raise TypeAgeError
        elif not self.MIN_AGE <= age <= self.MAX_AGE:
            raise ValueAgeError(age, self.MIN_AGE, self.MAX_AGE)

    def validate_phone_number(self, number: str) -> None:
        if not re.match(self.PHONE_NUMBER_PATTERN, number):
            raise PhoneNumberError

    def __set_name__(self, owner, name) -> None:
        self.name = "_" + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.name == "_age":
            validate_age(value, TenantDescriptor.MIN_AGE, TenantDescriptor.MAX_AGE)
        instance.__dict__[self.name] = value
