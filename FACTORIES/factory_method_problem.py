#Con el patron de builder haces outsourcing de la creación de un objeto
#Sin embargo en un patrón de Factory, esta clase es la única responsable
#de la creación completa de los objetos

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    #Si queremos un punto en coordenadas polares no podemos redefinir el constructor
    #def __init__(self, rho, theta):