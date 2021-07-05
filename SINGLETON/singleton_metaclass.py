#Una alternativa a utilizar el decorator es implementar un metaclase
#type es la metaclase de todas las clases. Por eso Singleton hereda de type y es ahí donde hacemos
#override del método __call__

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    

class Database(metaclass=Singleton):
    def __init__(self):
        print("Loading database")
    
if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print( d1 == d2)