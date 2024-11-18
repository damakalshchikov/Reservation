from classes.abstractions.abstarct_rentable import Rentable
from classes.tenants.tenant import Tenant
from exceptions.rentable_exceptions import FullReservationError
from exceptions.tenant_exceptions import HaveRentError


class RentalAgreement:
    """Класс для управления бронированием и отменой бронирования с несколькими арендаторами."""

    def __init__(self, rentable: Rentable, *tenants: Tenant):
        total_guests = len(tenants)
        self._rentable = rentable
        self._tenants = tenants
        self._guests_count = total_guests

        if total_guests > rentable.available_capacity:
            raise FullReservationError(self._rentable.name)

        self.__book()

    def __book(self) -> None:
        """Бронирует места для всех переданных арендаторов"""

        self._rentable.available_capacity -= self._guests_count

        for tenant in self._tenants:
            if tenant.has_rental():
                raise HaveRentError(self._rentable.address, tenant.first_name, tenant.last_name)
            tenant.attach_rental(self._rentable)

        print(
            f"Забронировано {self._guests_count} мест в '{self._rentable.name}' для арендаторов: "
            + ", ".join([f"{t.first_name} {t.last_name}" for t in self._tenants])
        )

    def cancel(self) -> None:
        """Отменяет бронирование и освобождает места для всех арендаторов"""

        self._rentable.available_capacity += self._guests_count

        for tenant in self._tenants:
            tenant.detach_rental()

        print(
            f"Бронирование {self._guests_count} мест в '{self._rentable.name}' отменено для арендаторов: "
            + ", ".join([f"{t.first_name} {t.last_name}" for t in self._tenants])
        )
