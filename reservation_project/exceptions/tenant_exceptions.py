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
