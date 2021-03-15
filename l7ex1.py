class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        output = '\n'.join(list(map(str, self.matrix)))
        return output

    def __add__(self, other):
        result = []
        for row in range(len(self.matrix)):
            row_result = []
            if len(self.matrix[row]) == len(other.matrix[row]):
                for column in range(len(self.matrix[row])):
                    row_result.append(self.matrix[row][column] +
                                      other.matrix[row][column])
                result.append(row_result)
            else:
                return Matrix([])
        return Matrix(result)


a = Matrix([[1, 2], [3, 4], [5, 6]])
print(a, '\n')
b = Matrix([[7, 1], [3, 4], [9, 0]])
print(b, '\n')
print(a + b)
