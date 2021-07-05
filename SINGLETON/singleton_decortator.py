#Si la clase requerida no está entre las instancias, la añadimos para saber cuales son las clases
#que han sido requeridas

def singleton(class_):
    instances = {}

    #Basicamente, lo que tenemos es un diccionario que se encarga de todas las instancias que
    # quieren ser un singleton
    def get_instance(*args,**kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    
    return get_instance

@singleton
class Database:
    def __init__(self) -> None:
        print("loading database")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()

    print(d1 == d2)

