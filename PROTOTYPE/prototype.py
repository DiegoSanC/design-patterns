import copy

class Adress:
    def __init__(self, street_address, city, country) -> None:
        self.city = city
        self.country = country
        self.street_address = street_address

    def __str__(self) -> str:
        return f"{self.street_address}, {self.city}, {self.country}"

class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} lives at {self.address}"

adress = Adress("123 London Road", "London", "UK")
john = Person("John", adress)
print(john)
jane = Person("Jane", adress)

#Jane moves
jane.address.street_address = "123B London Road"
#Al hacer esto estamos cambiando tambien el objeto de john porque ambos tienen una referencia
#al objeto Adrees, y lo estamos modificando
print(john)
print(jane)

adress = Adress("123 London Road", "London", "UK")
john = Person("John", adress)
jane = copy.deepcopy(john)
jane.name = "Jane"
jane.address.street_address = "123B London Road"
print(john)
print(jane)

adress = Adress("123 London Road", "London", "UK")
john = Person("John", adress)
#Copy si que va a capturar el cambio de nombre pero no el cambio de direccion porque es un shallow copy
jane = copy.copy(john)
jane.name = "Jane"
jane.address.street_address = "123B London Road"
print(john)
print(jane)