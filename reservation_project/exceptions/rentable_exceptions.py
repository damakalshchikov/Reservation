class FullReservationError(Exception):
    def __init__(self, rental_name: str) -> None:
        self.rental_name: str = rental_name

    def __str__(self) -> str:
        return f"""Арендуемый объект "{self.rental_name}" переполнен"""