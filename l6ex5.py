# 5. Реализовать класс Stationery (канцелярская принадлежность). 
# Определить в нем атрибут title (название) и метод draw (отрисовка). 
# Метод выводит сообщение “Запуск отрисовки.” 
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
# В каждом из классов реализовать переопределение метода draw. 
# Для каждого из классов методы должен выводить уникальное сообщение. 
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    
    def draw(self):
        print("Запуск отрисовки.")
    
class Pen(Stationery):
    def draw(self):
        super().draw()
        print("Pen write")

class Pencil(Stationery):
    def draw(self):
        super().draw()
        print("Pencil write")

class Handle(Stationery):
    def draw(self):
        super().draw()
        print("Handle write")


pen = Pen("pen")
pen.draw()

pencil = Pencil("pencil")
pencil.draw()

handle = Handle("handle")
handle.draw()