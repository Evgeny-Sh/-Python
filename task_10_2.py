from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def calc_cloth_amount(self):
        pass


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    def calc_cloth_amount(self):
        return self.__height * 2 + 0.3


class Coat(Clothes):
    def __init__(self, title, size):
        super().__init__(title)
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def height(self, size):
        self.__size = size

    def calc_cloth_amount(self):
        return self.__size/6.5 + 0.5


suit = Suit('Костюм', height=3)
print(suit.calc_cloth_amount())
suit.height = 4
print(suit.title, suit.height)
print(suit.calc_cloth_amount())

coat = Coat('Пальто', size=5)
print(coat.calc_cloth_amount())
coat.height = 4
print(coat.title, coat.height)
print(coat.calc_cloth_amount())

sum_cloth_amount = coat.calc_cloth_amount() + suit.calc_cloth_amount()
print(sum_cloth_amount)



