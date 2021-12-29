class ComplexNumber:
    def __init__(self, real, com=0):
        self.real = real
        self.com = com

    def __str__(self):
        return f'{self.real}{self.com:+}i'

    def __wrap(func):
        def wrapper(self, other):
            assert isinstance(other, (int, float, ComplexNumber)), 'second object is not number or complex number'
            if isinstance(other, (int, float)):
                other = ComplexNumber(other)
            return func(self, other)
        return wrapper

    @__wrap
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.com + other.com)

    @__wrap
    def __radd__(self, other):
        return ComplexNumber(self.real + other.real, self.com + other.com)

    @__wrap
    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.com * other.com,
                             self.real * other.com + self.com * other.real)
    @__wrap
    def __rmul__(self, other):
        return ComplexNumber(self.real * other.real - self.com * other.com,
                             self.real * other.com + self.com * other.real)


c_n_1 = ComplexNumber(2, 5)
c_n_2 = ComplexNumber(3, -2)

print(f'{c_n_1} + {c_n_2}= ', c_n_1 + c_n_2)
print(f'{c_n_1} * {c_n_2}= ', c_n_1 * c_n_2)
print(f'{c_n_1} + 4= ', c_n_1 + 4)
print(f'{c_n_1} * 3= ', c_n_1 * 3)
print(f'3 + {c_n_1}= ', 3 + c_n_1)
print(f'4 * {c_n_1}= ', 4 * c_n_1)

