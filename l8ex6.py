class WarehouseOfficeoEquipment:
    """Склад оргтехники"""

    def __init__(self):
        self.col = []
        self.company = []
        self.count_product = 0
        self.count_for_type = {}


    def add_to_warehouse(self, product):
        """добавление продукта на склад"""
        self.col.append(product.__dict__)
        self.count_product += 1
        if product.name in self.count_for_type.keys():
            self.count_for_type[product.name] += 1
        else:
            self.count_for_type[product.name] = 1


    def remove_to_warehouse(self, product):
        """Удаляем со склада позицию"""
        id = self.col.index(product.__dict__)
        self.col.pop(id)
        self.count_product -= 1
        self.count_for_type[product.name] -= 1

    def ship_to_company(self, product, company):
        """Метод отправки товара на компанию"""
        if product.__dict__ in self.col:
            self.company.append({company:product.__dict__})
            self.remove_to_warehouse(product)



class BadType(Exception):

    def __init__(self, message = "Bad Price"):
        self.txt = message

    def __str__(self):
        return self.txt


class OfficeEquipment:
    """Оргтехника"""

    def __init__(self, brand, name,  price):
        self.brand = brand
        self.name = name
        if type(price) == float or type(price) == int:
            self.price = price
        else:
            raise BadType


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
        super().__init__(brand, name, price)
        self.coppy_speed = coppy_speed
        self.max_format = max_format


mita1330 = Coppier("Mita", "MFC 1330" ,500, 12, "A3")
mita1130 = Printer("Mita", "MFP 1130", 300, 30, "A4")
sklad = WarehouseOfficeoEquipment()
sklad.add_to_warehouse(mita1130)
sklad.add_to_warehouse(mita1130)
sklad.add_to_warehouse(mita1330)
print(sklad.__dict__)
sklad.ship_to_company(mita1130,"ABC")
sklad.ship_to_company(mita1330,"ABC")
print(sklad.__dict__)
