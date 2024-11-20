import json
import xml.etree.ElementTree as ET

from classes.tenants.tenant import Tenant


class TenantMenager:
    """CRUD-менеджер для управления объектами Tenant"""

    def __init__(self):
        self.tenant_list: list[Tenant] = []

    def create(self, first_name: str, last_name: str, age: int, money: int | float, phone_number: str) -> Tenant:
        """Создаёт и добавляет объект Tenant"""

        tenant = Tenant(first_name, last_name, age, money, phone_number)
        self.tenant_list.append(tenant)
        return tenant

    def read_all(self) -> list[Tenant]:
        """Возвращает список всех объектов Tenant"""
        return self.tenant_list

    def read_by_id(self, tenant_id: int) -> Tenant:
        """Возвращает Tenant объект по его ID"""

        for tenant in self.tenant_list:
            if tenant.tenant_id == tenant_id:
                return tenant
        # Добавить собственное исключение

    def update(self, tenant_id: int, first_name: str | None = None, last_name: str | None = None,
               age: int | None = None, money: int | float | None = None, phone_number: str | None = None) -> None:
        """Обновляет атрибуты Tenant объекта по его ID"""

        try:
            tenant: Tenant = self.read_by_id(tenant_id)
        except Exception:
            print("Невозможно удалить несуществующий объект")
        else:
            tenant.first_name = first_name if first_name else tenant.first_name
            tenant.last_name = last_name if last_name else tenant.last_name
            tenant.age = age if age else tenant.age
            tenant.money = money if money else tenant.money
            tenant.phone_number = phone_number if phone_number else tenant.phone_number

    def delete(self, tenant_id: int) -> None:
        """Удаляет Tenant объект по его ID"""

        try:
            tenant: Tenant = self.read_by_id(tenant_id)
        except Exception:
            print("Невозможно удалить несуществующий объект")
        else:
            self.tenant_list.remove(tenant)

    def save_to_json(self, filename: str) -> None:
        """Сохраняет список объектов Tenant в JSON файл"""

        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(
                [
                    tenant.to_dict() for tenant in self.tenant_list
                ],
                json_file,
                ensure_ascii=False,
                indent=4
            )

    def load_from_json(self, filename: str) -> None:
        """Загружает список объектов Tenant из JSON файла"""

        with open(filename, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        for obj_data in data:
            obj_data.pop("id"), obj_data.pop("place_of_residence")
            self.create(**obj_data)

    def save_to_xml(self, filename: str) -> None:
        """Сохраняет список объектов Tenant в XML файл"""

        root = ET.Element("Tenants")

        for tenant in self.tenant_list:
            tenant_elem = ET.SubElement(root, "Tenant")
            for key, value in tenant.to_dict().items():
                child = ET.SubElement(tenant_elem, key)
                child.text = str(value) if value is not None else ""

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    def load_from_xml(self, filename: str) -> None:
        """Загружает список объектов Tenant из XML файла"""

        tree = ET.parse(filename)
        root = tree.getroot()

        for tenant_elem in root.findall("Tenant"):
            tenant_data = {child.tag: child.text for child in tenant_elem}
            # Преобразуем данные
            tenant_data["age"] = int(tenant_data["age"])
            tenant_data["money"] = float(tenant_data["money"])
            tenant_data.pop("id"), tenant_data.pop("place_of_residence")
            self.create(**tenant_data)
