class Road:
    def __init__(self, length, width):
        self._mass_1cm = 3000
        self._thickness = 12
        self._length = length
        self._width = width
        self.mass = None

    def mass_calc(self):
        self.mass = self._length * self._width * self._mass_1cm * self._thickness
        print(f'Road mass: {self.mass} kg')


if __name__ == '__main__':
    road = Road(100, 10)
    road.mass_calc()
