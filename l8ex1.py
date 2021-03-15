class Data:
    """dd-mm-yyyy"""

    def __init__(self, data_string):
        self.data = data_string

    @classmethod
    def data_to_int(cls, date: "Data"):
        return list(map(int, date.data.split("-")))

    @staticmethod
    def validation(date: "Data"):
        check_list = [int(x) for x in list(date.data.split("-")) \
                      if x.isnumeric()]
        if len(check_list) != 3:
            raise ValueError("Неверная строка")
        elif not 0 < check_list[0] < 32:
            raise ValueError("Некорректный день")
        elif not 0 < check_list[1] < 13:
            raise ValueError("Некорректный месяц")
        print("Проверка пройдена")
        return True


the_data = Data("01-03-1988")
if the_data.validation(the_data):
    print(Data.data_to_int(the_data))

the_data2 = Data("a1-13-200")
if the_data2.validation(the_data2):
    print(Data.data_to_int(the_data2))


