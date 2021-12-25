class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    def __str__(self):
        s = '\n'.join(['\t'.join([str(i) for i in j]) for j in self.matrix])
        return s

    def __add__(self, other):
        assert type(other) == Matrix, 'second element is not a matrix'
        res = [[i + oi for i, oi in zip(j, oj)] for j, oj in zip(self.matrix, other.matrix)]
        return Matrix(res)


m1 = Matrix([[1, 2, 3], [3, 499, -5], [4, 6, 18]])
print('m1:\n', m1, sep='')

m2 = Matrix([[-1, -2, -3], [-3, -499, 5], [1, 2, 10]])
print('m2:\n', m2, sep='')

m3 = m1 + m2
print('m3:\n', m3, sep='')

print(m1 + 3)

