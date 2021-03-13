class WarehouseOfficeoEquipment:
    """Склад оргтехники"""

    def __init__(self):
        self.col = []
        self.company = []

    def add_to_warehouse(self, product):
        """добавление продукта на склад"""
        self.col.append(product.__dict__)

    def ship_to_company(self, product, company):
        """Метод отправки товара на компанию"""
        if product.__dict__ in self.col:
            self.company.append({company:product.__dict__})

class OfficeEquipment:
    """Оргтехника"""

    def __init__(self, brand, name,  price):
        self.brand = brand
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, brand, name, price, print_speed, max_format):
        super().__init__(brand, name, price)
        self.print_speed = print_speed
        self.max_format = max_format


class Scanner(OfficeEquipment):
    def __init__(self, brand, name, price, scan_speed, max_format):
        super().__init__(brand, name, price)
        self.scan_speed = scan_speed
        self.max_format = max_format


class Coppier(OfficeEquipment):
    def __init__(self, brand, name, price, coppy_speed, max_format):
        super().__init__(self, brand, name, price)
        self.coppy_speed = coppy_speed
        max_format = max_format


mita1130 = Printer("Mita", "MFP 1130", 300, 30, "A4")
sklad = WarehouseOfficeoEquipment()
sklad.add_to_warehouse(mita1130)
sklad.add_to_warehouse(mita1130)
sklad.add_to_warehouse(mita1130)
print(sklad.__dict__)
sklad.ship_to_company(mita1130,"ABC")
sklad.ship_to_company(mita1130,"ABC")
print(sklad.__dict__)

