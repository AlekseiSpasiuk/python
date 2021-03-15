class ListNumeric(Exception):
    """Исключение не числовой список"""

    def __init__(self, message="Не числовой список"):
        self.message = message

    def __str__(self):
        return self.message


def is_numeric_list(input_list):
    output_list = [int(x) for x in input_list if x.isnumeric()]
    if len(output_list) != len(input_list):
        raise ListNumeric
    return output_list


in_list = []
print("input :q to exit")

while(True):
    new = input()
    if new == ':q':
        break
    in_list.append(new)

try:
    print(is_numeric_list(in_list))

except ListNumeric as err:
    print(err)
    print(in_list)
