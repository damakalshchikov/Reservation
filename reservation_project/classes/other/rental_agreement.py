from classes.abstractions.abstarct_rentable import Rentable
from classes.tenants.tenant import Tenant
from exceptions.agreement_exceptions import BudgetError, FullReservationError
from exceptions.agreement_exceptions import HaveRentError


class RentalAgreement:
    """Класс для управления бронированием и отменой бронирования с несколькими арендаторами."""

    def __init__(self, rentable: Rentable, nights: int, *tenants: Tenant):
        total_guests = len(tenants)
        self._rentable = rentable
        self._nights = nights
        self._tenants = tenants
        self._guests_count = total_guests

        if total_guests > rentable.available_capacity:
            raise FullReservationError(self._rentable.name, self._rentable.available_capacity)

        self.__chek_budget()
        self.__book()

    def __chek_budget(self) -> None:
        """Проверка на то, хватает ли бюджета для бронирования"""

        total_budget: int | float = sum(tenant.money for tenant in self._tenants)
        total_cost: int | float = self._rentable.price_per_night * self._nights

        if total_budget < total_cost:
            raise BudgetError(self._rentable.name, total_budget, total_cost)

    def __book(self) -> None:
        """Бронирует места для всех переданных арендаторов"""

        self._rentable.available_capacity -= self._guests_count

        for tenant in self._tenants:
            if tenant.has_rental():
                raise HaveRentError(self._rentable.address, tenant.first_name, tenant.last_name)
            tenant.attach_rental(self._rentable)

        print(
             f"""Забронировано {self._guests_count} мест в "{self._rentable.name}" """
            f"""на {self._nights} ночей для арендатора/ов: """
            + ", ".join([f"{t.first_name} {t.last_name}" for t in self._tenants])
        )

    def cancel(self) -> None:
        """Отменяет бронирование и освобождает места для всех арендаторов"""

        self._rentable.available_capacity += self._guests_count

        for tenant in self._tenants:
            tenant.detach_rental()

        print(
            f"""Бронирование {self._guests_count} мест в "{self._rentable.name}" отменено для арендатора/ов: """
            + ", ".join([f"{t.first_name} {t.last_name}" for t in self._tenants])
        )
