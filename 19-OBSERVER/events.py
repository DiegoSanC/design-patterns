"""
Es probablemente el patron de diseño mas comun:
Necesitamos ser avisados de que ciertas cosas están pasando:
    -las propiedas de un objeto cambian
    -un objeto hace algo
    -ocurre un evento externo
Escuchamos eventos y notificamos
La entidad que genera los eventos es el "observable"

"""
class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)

class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.falls_ill = Event()


    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


def call_doctor(name, address):
    print(f"{name} needs a doctor at {address}")


if __name__ == "__main__":
    person = Person("Perdo", "222B Baker Str")
    person.falls_ill.append(
        lambda name, address: print(f"{name} is ill")
    )
    person.falls_ill.append(call_doctor)
    person.catch_a_cold()
    
    person.falls_ill.remove(call_doctor)
    person.catch_a_cold()