class ObjectNotFound(Exception):
    """Исключение того, что объект не найден"""

    def __str__(self) -> str:
        return "Объект не найден"
