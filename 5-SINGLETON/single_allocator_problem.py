import random

#Problema: A pesar de que sobreescribimos el método __new__ para que solo instancie una vez
#la clase (podemos comprobar que d1 apunta al mismo objeto que d2) el método __init__ es llamado
#dos veces. Si la inicializacion del objeto fuese muy costosa computacionalmente, podríamos 
#estar perdiendo un tiempo valioso en la segunda llamada cuando no está sirviendo para nada.
#La segunda llamada se produce porque trás llamar al metodo __new__ que es el que crea la clase, 
#se llama automaticamente al init para instanciarla.

class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1,101)
        print("id: {}".format(id))

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance



if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)