class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__('Penn')

    def draw(self):
        print('Pen is drawing.')


class Pencil(Stationery):
    def __init__(self):
        super().__init__('Pencil')

    def draw(self):
        print('Pencil is drawing.')


class Handle(Stationery):
    def __init__(self):
        super().__init__('Handle')

    def draw(self):
        print('Handle is drawing.')


for cl in (Stationery, Pen, Pencil, Handle):
    cl_i = cl()
    print(cl_i.title)
    cl_i.draw()
