class BudgetError(Exception):
    """Исключение, если бюджет арендаторов недостаточен для бронирования"""

    def __init__(self, rentable_name: str, budget: int | float, cost: int | str):
        self.rentable_name: str = rentable_name
        self.budget: int | float = budget
        self.cost: int | float = cost

    def __str__(self):
        return (f"Недостаточно средств для бронирования {self.rentable_name}."
                f"Необходимая сумма: {self.cost}, доступная сумма: {self.budget}")

class FullReservationError(Exception):
    """Исключение о переполнении арендуемого объекта"""

    def __init__(self, rental_name: str, avaible_capacity: int):
        self.rental_name: str = rental_name
        self.avaible_capacity: int = avaible_capacity

    def __str__(self) -> str:
        return f"""Арендуемый объект "{self.rental_name}" переполнен. В нём всего доступно {self.avaible_capacity} мест"""
