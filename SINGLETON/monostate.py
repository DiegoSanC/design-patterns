#Un monostate es una variacion del singleton donde pones todo el estado de un objeto
#en una variable estática

class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 55
    }

    def __init__(self):
        #Aqui estamos apuntando a la misma referencia para todos los objetos instanciados
        self.__dict__ = self.__shared_state

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"
    

class Monostate:
    __shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ""
        self.money_managed = 0

    def __str__(self) -> str:
        return f"{self.name} manage {self.money_managed}$"



if __name__ == "__main__":
    ceo1 = CEO()
    print(ceo1)

    ceo2 = CEO()
    #Estamos cambiando ambos objetos porque compartendio un estado estático que es __shared_state
    ceo2.age = 77  
    print(ceo1)
    print(ceo2)

    cfo1 = CFO()
    cfo1.name = "Sheryl"
    cfo1.money_managed = 1 
    print(cfo1)
    cfo2 = CFO()
    cfo2.name = "Ruth"
    cfo2.money_managed = 10
    print(cfo1)
    print(cfo2)