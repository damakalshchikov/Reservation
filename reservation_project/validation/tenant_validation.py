from exceptions.tenant_exceptions import TypeAgeError, ValueAgeError


def validate_age(age: int, min_age: int, max_age: int) -> None:
    if not isinstance(age, int):
        raise TypeAgeError
    elif not min_age <= age <= max_age:
        raise ValueAgeError(age, min_age, max_age)
