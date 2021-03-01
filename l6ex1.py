# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# реализовал автоматическую работу в обратном направлении и попытался реализовать максимально удобный
# для наследования и последующего использования класс 
class TrafficLight:
    def __init__(self, color):
        self.__color = "red"
        self.__reverce = False
        self.__order_list = ["red", "yelow", "green"]
        self.__dict_time = {"red": 7, "yelow": 2, "green": 5}

    def __get_next_color(self):
        num_color = self.__get_num_color(self.__color)
        if self.__reverce:
            num_color -= 1
        elif not self.__reverce:
            num_color += 1
        if 0 <= num_color < len(self.__order_list):
            return self.__order_list[num_color]
        else:
            self.__switch_reverce()
            return self.__get_next_color()

    def __get_time(self, color):
        return self.__dict_time[color]

    def __in_order(self, color):
        return color in self.__order_list

    def __get_num_color(self, color):
        return self.__order_list.index(color)

    def __check_order(self, color):
        return color == self.__get_next_color()

    def __switch_reverce(self):
        self.__reverce = not self.__reverce

    def __lighting(self):
        return f"light {self.__color} {self.__get_time(self.__color)} sec"

    def running(self, color = None):
        if not color:
            color = self.__get_next_color() 
        if not self.__in_order(color):
            return "wrong color"
        if not self.__check_order(color):
            return "wrong order"
        self.__color = color
        return self.__lighting()


semafor = TrafficLight("red")
print(semafor.running("red"))
print(semafor.running("yelow"))
print(semafor.running("green"))
print(semafor.running("yelow"))
print(semafor.running("red"))
print(semafor.running("white"))
print(semafor.running(""))
print(semafor.running(""))
print(semafor.running(""))
print(semafor.running(""))
print(semafor.running(""))
