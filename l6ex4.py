# 4. Реализуйте базовый класс Car. 
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
# остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
# Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. 
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f"{self.name} go"

    def stop(self):
        return f"{self.name} stop" 

    def turn(self, direction):
        return f"{self.name} turn {direction}"

    def show_speed(self):
        return f"{self.name} speed {self.speed}"

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Warning! Your town car {self.name} speed {self.speed} more 60!"
        else:
            return f"{self.name} speed {self.speed}"

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Warning! Your work car {self.name} speed {self.speed} more 40!"
        else:
            return f"{self.name} speed {self.speed}"

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

class SportCar(Car):
    pass

police_car = PoliceCar(100, 'red', '47ot')
print(police_car.go())
print(police_car.is_police, police_car.speed)
print(police_car.turn("left"))
print(police_car.turn("right"))
print(police_car.show_speed())
print(police_car.stop())

work_car = WorkCar(100, 'yellow', 'road worker')
print(work_car.go())
print(work_car.show_speed())
print(work_car.is_police, police_car.speed)
print(work_car.turn("left"))
print(work_car.turn("right"))
print(work_car.stop())



