class Cell:

    def __init__(self, quantity: int):
        self.quantity = quantity

    def __str__(self):
        return f"Cell in {self.quantity}"

    def __add__(self, other):
        """Сложение.
        Объединение двух клеток.
        При этом число ячеек общей клетки должно равняться сумме ячеек
        исходных двух клеток."""
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        """Вычитание.
        Участвуют две клетки.
        Операцию необходимо выполнять только
        если разность количества ячеек двух клеток больше нуля,
        иначе выводить соответствующее сообщение."""
        if self.quantity - other.quantity > 0:
            return Cell(self.quantity - other.quantity)
        else:
            print("Operation's inposible, difference < 0")
            return(Cell(0))

    def __mul__(self, other):
        """Умножение.
        Создается общая клетка из двух.
        Число ячеек общей клетки определяется как
        произведение количества ячеек этих двух клеток."""
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        """Деление.
        Создается общая клетка из двух.
        Число ячеек общей клетки определяется как целочисленное деление
        количества ячеек этих двух клеток."""
        if other.quantity:
            return Cell(self.quantity // other.quantity)
        else:
            print("Division by zero")

    def make_order(self, cell_in_row):
        res = ['*' if x % cell_in_row != 0 else '*\n'
                for x in range(1, self.quantity + 1)]
        return ''.join(res)


a = Cell(10)
b = Cell(20)
print(a + b)
print(a - b)
print(b - a)
print(a * b)
print(b / a)

print(b.make_order(7))
