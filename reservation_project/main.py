from classes.other.rental_agreement import RentalAgreement
from classes.reservation_objects.rentable import Apartment
from classes.tenants.tenant import Tenant


# Пример бронирования жилья арендаторами
apartment = Apartment(1, "Квартира в центре", "ул. Центральная, д. 10", 4500.0, 3)
apartment2 = Apartment(2, "dfsds", "dad", 4, 1)
tenant1 = Tenant("Анна", "Петрова", 32, "+79005554433")
tenant2 = Tenant("Максим", "Сидоров", 29, "+79007776655")
tenant3 = Tenant("Ольга", "Кузнецова", 35, "+79001234567")


agreement = RentalAgreement(apartment, tenant1, tenant2, tenant3)
agreement.cancel()
