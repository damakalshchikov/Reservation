from classes.abstractions.abstarct_rentable import Rentable
from classes.tenants.tenant import Tenant


class RentalAgreement:
    """Класс для управления бронированием и отменой бронирования с несколькими арендаторами."""

    def __init__(self, rentable: Rentable, *tenants: Tenant):
        total_guests = len(tenants)

        if total_guests > rentable._available_capacity:
            raise ValueError("Недостаточно свободных мест для бронирования.")

        self._rentable = rentable
        self._tenants = tenants
        self._guests_count = total_guests
        self.__book()

    def __book(self) -> None:
        """Бронирует места для всех переданных арендаторов"""
        self._rentable._available_capacity -= self._guests_count
        for tenant in self._tenants:
            if tenant.has_rental():
                raise ValueError(f"Арендатор {tenant._first_name} {tenant._last_name} уже арендует жильё")
            tenant.attach_rental(self._rentable)  # По умолчанию бронируем 1 место на каждого арендатора
        print(
            f"Забронировано {self._guests_count} мест в '{self._rentable._name}' для арендаторов: "
            + ", ".join([f"{t._first_name} {t._last_name}" for t in self._tenants])
        )

    def cancel(self) -> None:
        """Отменяет бронирование и освобождает места для всех арендаторов"""
        if self._guests_count > (self._rentable._capacity - self._rentable._available_capacity):
            raise ValueError("Невозможно отменить бронирование больше, чем было забронировано.")

        self._rentable._available_capacity += self._guests_count
        for tenant in self._tenants:
            tenant.detach_rental()
        print(
            f"Бронирование {self._guests_count} мест в '{self._rentable._name}' отменено для арендаторов: "
            + ", ".join([f"{t._first_name} {t._last_name}" for t in self._tenants])
        )
