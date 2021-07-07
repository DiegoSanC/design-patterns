from abc import ABC
from enum import Enum, auto

class HotDrink(ABC):
    def consume(self):
        pass

class Tea(HotDrink):
    def consume(self):
        print("this tea is delicious")

class Coffe(HotDrink):
    def consume(self):
        print("This coffe is delicious")


class HotDrinkFactory(ABC):
    def prerpare(self, amount):
        pass

class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Put in tea bag, boil water,"
        f" put {amount} ml, enjoy!")

        return Tea()

class CoffeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffe()


def make_drink(type):
    if type == "tea":
        return TeaFactory().prerpare(200)
    elif type == "coffe":
        return CoffeFactory().prerpare(50)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self) -> None:
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Available drinks")
        for f in self.factories:
            print(f[0])
        s = input(f"Please pick drink (0-{len(self.factories) - 1}): ")
        idx = int(s)
        s = input(f"Specify amount: ")
        amount = int(s)

        return self.factories[idx][1].prepare(amount)



if __name__ == "__main__":
    # entry = input("What you want to drink ")
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    hdm.make_drink()