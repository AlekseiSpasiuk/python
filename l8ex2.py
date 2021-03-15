class MyDevisionError(Exception):
    """ x / 0 """

    def __init__(self, message="Деление на ноль"):
        self.message = message

    def __str__(self):
        return self.message


def div(a, b):
    if b == 0:
        raise MyDevisionError
    return a / b


try:
    div(1, 0)
except MyDevisionError as err:
    print(err)
