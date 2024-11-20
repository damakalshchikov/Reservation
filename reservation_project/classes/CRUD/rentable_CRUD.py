import json
import xml.etree.ElementTree as ET
from abc import ABCMeta

from classes.abstractions.abstarct_rentable import Rentable
from classes.reservation_objects.rentable import Apartment, House, Room


class RentableMenager:
    """CRUD-менеджер для управления объектами Rentable"""

    __class_names: dict[str, ABCMeta] = {
        "Room": Room,
        "Apartment": Apartment,
        "House": House
    }

    def __init__(self):
        self.rentable_list: list[Rentable] = []

    def create(self, class_name: ABCMeta, name: str, address: str, price_per_night: int | float) -> Rentable:
        """Создаёт и добавляет объект Rentable список"""

        result: Rentable = class_name(name=name, address=address, price_per_night=price_per_night)
        self.rentable_list.append(result)
        return result

    def read_all(self):
        """Возвращает список всех объектов Rentable"""

        return self.rentable_list

    def read_by_id(self, rentable_id: int) -> Rentable:
        """Возвращает Rentable объъект по его ID"""

        for rentable in self.rentable_list:
            if rentable.rentable_id == rentable_id:
                return rentable
        # Добавить собственное исключение

    def update(self, rentable_id: int, name: str| None, address: str| None = None, price_per_night: int | float | None = None) -> None:
        """Обновляет атрибуты Rentable объекта по его ID"""

        try:
            rentable_obj: Rentable = self.read_by_id(rentable_id)
        except Exception:
            print("Невозможно обновить несуществующий объект")
        else:
            rentable_obj.name = name if name else rentable_obj.name
            rentable_obj.address = address if address else rentable_obj.address
            rentable_obj.price_per_night = price_per_night if price_per_night else rentable_obj.price_per_night


    def delete(self, rentable_id: int) -> None:
        """Удаляет Rentable объект по его ID"""

        try:
            rentable_obj: Rentable = self.read_by_id(rentable_id)
        except Exception:
            print("Невозможно удалить несуществующий объект")
        else:
            self.rentable_list.remove(rentable_obj)

    def save_to_json(self, filename: str) -> None:
        """Сохраняет список объектов Rentable в JSON файл"""

        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(
                [
                    {"class_name": obj.__class__.__name__, **obj.to_dict()}
                    for obj in self.rentable_list
                ],
                json_file,
                ensure_ascii=False,
                indent=4
            )

    def load_from_json(self, filename: str) -> None:
        """Загружает список объектов Rentable из JSON файла"""

        with open(filename, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        for obj_data in data:
            class_name = obj_data.pop("class_name", None)
            cls = class_names.get(class_name)
            if cls:
                self.create(cls, **obj_data)

    def save_to_xml(self, filename: str) -> None:
        """Сохраняет список объектов Rentable в XML файл"""

        root = ET.Element("Rentables")
        for obj in self.rentable_list:
            obj_elem = ET.SubElement(root, obj.__class__.__name__)
            for key, value in obj.to_dict().items():
                child = ET.SubElement(obj_elem, key)
                child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

    def load_from_xml(self, filename: str) -> None:
        """Загружает список объектов Rentable из XML файла"""

        tree = ET.parse(filename)
        root = tree.getroot()
        for obj_elem in root:
            cls = class_names.get(obj_elem.tag)
            if cls:
                obj_data = {child.tag: child.text for child in obj_elem}
                # Преобразование типов
                obj_data["price_per_night"] = float(obj_data["price_per_night"])
                self.create(cls, **obj_data)
