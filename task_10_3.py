class Cell:
    def __init__(self, internal_cells: int):
        if isinstance(internal_cells, int) and internal_cells >= 0:
            self.internal_cells = internal_cells
        else:
            raise ValueError('Number of internal cells should be non-negative integer')

    def __wrap(func):
        def wrapper(self, other):
            assert type(other) == Cell, 'second object is not cell'
            return func(self, other)
        return wrapper

    @__wrap
    def __add__(self, other):
        return Cell(self.internal_cells + other.internal_cells)
    
    @__wrap
    def __sub__(self, other):
        if self.internal_cells <= other.internal_cells:
            raise ValueError('Number of internal cells in first cell should be not less than in second cell')
        return Cell(self.internal_cells - other.internal_cells)
    
    @__wrap
    def __mul__(self, other):
        return Cell(self.internal_cells * other.internal_cells)
    
    @__wrap
    def __floordiv__(self, other):
        return Cell(self.internal_cells // other.internal_cells)
    
    @__wrap
    def __truediv__(self, other):
        return self.__floordiv__(other)

    def make_order(self, n):
        res = '\n'.join(["*" * n] * (self.internal_cells // n))
        if self.internal_cells // n:
            res += '\n'
        if self.internal_cells % n:
            res += "*" * (self.internal_cells % n)
        return res


c1 = Cell(12)
print(c1.make_order(5))
c2 = Cell(7)
print('+:', (c1 + c2).internal_cells, (c1 + c2).make_order(10), sep='\n')
print('-:', (c1 - c2).internal_cells,  (c1 - c2).make_order(10), sep='\n')
print('*:', (c1 * c2).internal_cells,  (c1 * c2).make_order(10), sep='\n')
print('/:', (c1 / c2).internal_cells,  (c1 / c2).make_order(10), sep='\n')

# test that only cells can be summed
c1 + 2
