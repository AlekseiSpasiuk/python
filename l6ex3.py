# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: 
# name, surname, position (должность), income (доход). 
# Последний атрибут должен быть защищенным и ссылаться на словарь, 
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
# Создать класс Position (должность) на базе класса Worker. 
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
# и дохода с учетом премии (get_total_income). 
# Проверить работу примера на реальных данных 
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, 
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
    
class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"
    
    def get_total_income(self):
        return self._income["wage"]+self._income["bonus"]

# income = {"wage": wage, "bonus": bonus}

director = Position("Vasya", "Popov", "director", {"wage": 1000, "bonus": 500})
manager = Position("Vasya", "Ropov", "manager", {"wage": 200, "bonus": 1500})
worker_1 = Position("Vasya", "Topov", "worker", {"wage": 300, "bonus": 700})
worker_2 = Position("Vasya", "Sopov", "worker", {"wage": 100, "bonus": 400})
print(director.get_full_name())
print(director.get_total_income())
print(manager.get_full_name())
print(manager.get_total_income())
