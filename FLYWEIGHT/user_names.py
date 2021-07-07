#FlyWeight Motivation: 
"""
Esencialmente se trata una técnica de optimización del espacio => intenta ahorra memoria
 -Avoid redundancy when storing data => MMORPG -> no tiene sentido guardar los mismos nombres una
 y otra vez. Es más sencillo guardar una lista
 
 -Formato de texto -> en lugar de tener un formato para cada caracter guardamos el rango de letras
 sobre el que se aplica

"""
import string
import random

class User:
    def __init__(self, name) -> None:
        self.name = name
    

class User2:
    strings = []

    def __init__(self, full_name) -> None:
        def get_or_add(s):
            if s in self.strings:
                return self.strings.index(s)
            else:
                self.strings.append(s)
                return len(self.strings) - 1

        self.names = [get_or_add(x) for x in full_name.split(' ')]

    def __str__(self) -> str:
        return ' '.join([self.strings[x] for x in self.names])


def random_string():
    chars = string.ascii_lowercase
    return "".join([random.choice(chars) for i in range(8)])

if __name__ == "__main__":
    users = []
    users_2 = []
    #Si tenemos una clase User que apunta el nombre de cada usuario tenemos un producto cartesiano
    #de nombres almacenados en memoria
    first_names = [random_string() for i in range(100)]
    last_names = [random_string() for i in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User(f'{first} {last}'))
            users_2.append(User2(f'{first} {last}'))

    print(users_2[100])
