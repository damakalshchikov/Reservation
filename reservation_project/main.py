from classes.CRUD.tenant_CRUD import TenantMenager
from classes.CRUD.rentable_CRUD import RentableMenager
from classes.other.rental_agreement import RentalAgreement
from classes.reservation_objects.rentable import Apartment, Room, House
from classes.tenants.tenant import Tenant
from exceptions.CRUD_exceptions import ObjectNotFound
from exceptions.agreement_exceptions import HaveRentError
from exceptions.rental_exceptions import TypeNameRentalError
from exceptions.tenant_exceptions import ValueAgeError


# Создаём CRUD-менеджеры для управления Rentable и Tenant объектами
tenant_menager: TenantMenager = TenantMenager()
rentable_menager: RentableMenager = RentableMenager()


"""
Пример инициализации Rentable и Tenant объектов без возникновения исключений
"""

# Инициализируем арендаторов
tenant1: Tenant = tenant_menager.create("Михаил", "Дамакальщиков", 19, float("inf"), "89000000000")
tenant2: Tenant = tenant_menager.create("Игорь", "Петров", 45, 15000, "89005553535")
tenant3: Tenant = tenant_menager.create("Вася", "Пупкик", 20, 3000, "+79005002010")

# Инициализируем Rentable объекты
aparnment: Apartment = rentable_menager.create(Apartment, "Квартира в ЖК 'VIP-супер-крутость'", "г. Москва, ул. Лубянка, д. 1", 5000)
room: Room = rentable_menager.create(Room, "Комната в отеле", "г. Санкт-Петербург, пр-т. Лиговский, д. 2", 1500)
house: House = rentable_menager.create(House, "Домик в горах", "посёлок городского типа 'Красная Поляна'", 5000)


"""
Пример инициализации Tenant объекта с обработкой исключений
"""

try:
    # Инициализируем арендатора с возрастом меньше 18 лет
    tenant: Tenant = tenant_menager.create("Алексей", "Попович", 17, 5000, "89000000002")
except ValueAgeError as e:
    print(e)


"""
Пример инициализации Rentable объекта с обработкой исключений
"""

try:
    # Название Rentable объекта не строка
    VIP_house: House = rentable_menager.create(House, 123, "Какой-то адрес", 10000)
except TypeNameRentalError as e:
    print(e)


"""
Пример заключения договора аренды
"""

rentable_agreement1: RentalAgreement = RentalAgreement(aparnment, 2, tenant1, tenant2)


"""
Пример заключения договора аренды с исключением
"""

try:
    # tenant1 уже имеет забронированное жильё
    rentable_agreement2: RentalAgreement = RentalAgreement(house, 1, tenant1, tenant3)
except HaveRentError as e:
    print(e)


"""
Пример изменения tenant1 с помощью CRUD-менеджера
"""

tenant_menager.update(1, money=0)
print()
print(tenant1)


"""
Пример удаления tenant1 с помощью CRUD-менеджера, при возникновении исключения
"""

try:
    tenant_menager.delete(100)
except ObjectNotFound as e:
    print(e)


"""
Сохранение Rentable и Tenant объектов в JSON и XML
"""

rentable_menager.save_to_json("reservation_project/data/json/rentable.json")
rentable_menager.save_to_xml("reservation_project/data/xml/rentable.xml")

tenant_menager.save_to_json("reservation_project/data/json/tenant.json")
tenant_menager.save_to_xml("reservation_project/data/xml/tenant.xml")

tenant_menager.load_from_json("reservation_project/data/json/tenant.json")

