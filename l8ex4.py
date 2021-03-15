class WarehouseOfficeoEquipment:
    """Склад оргтехники"""

    def __init__(self, col):
        self.col = col


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

print(mita1130)
