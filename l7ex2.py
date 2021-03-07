from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def expenditure(self):
        pass

    def __add__(self, other):
        return self.expenditure + other.expenditure


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def expenditure(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, growth):
        self.growth = growth

    @property
    def expenditure(self):
        return 2 * self.growth + 0.3


coat = Coat(60)
suit = Suit(190)

print(coat.expenditure)
print(suit.expenditure)
print(coat + suit)
