#ISP
# La idea es muy sencilla: No deber añadir muchos métodos dentro de una interfaz

#Imaginemos que damos soporte para crear una impresora multifucion
class Machine:

    def print(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):

    def print(self, document):
        pass
    def fax(self, document):
        pass
    def scan(self, document):
        pass

#Si solo tenemos la interfaz machine pero esta clase de impresora no puede hacer uso de los métodos
# fax y scan tenemos un problema, porque aunque dejemos las funciones fax y scan sin implementar con
# un simple pass, si alguien instancia un objeto de tipo OldFashionedPrinter seguirá viendo los métodos
# de la interfaz y podría acabar haciendo llamadas a estos cuando estos no hacen nada.
class OldFashionedPrinter(Machine):
    def print(self, document):
        #ok
        pass

    def fax(self, document):
        pass # do nothing

    def scan(self, document):
        """ not supported!
        """
        raise NotImplementedError("Printer cannot scan!")
        #Este enfoque es un problema si esta pieza está dentro de un sistema muy grande


#Hay que hacerlo mas granular

class Printer:
    @abstractmethod
    def print(self, document):
        pass

class Scanner:
    @abstractmethod
    def scan(self, document):
        pass

class Fax:
    @abstractmethod
    def scan(self, document):
        pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)
    def scan(self, document):
        pass

#Si necesitamos una maquina multifunción, como por ejemplo la fotocopiadora, podemos implementar
#una clase que implemente las interfaces que proporcionen soporte a las diferentes funciones pero 
#dejamos dichas funciones como metodos abstractos, convirtiendo esta clase que implementa interfaces
# a su vez en otra interfaz:

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass
    @abstractmethod
    def scan(self, document):
        pass

class MultiFunctionMachine(MultiFunctionDevice):
    def print(self, document):
        print(document)
    def scan(self, document):
        pass

#Podríamos implementar los métodos de esta ultima clase, pero tambien podemos hacer lo siguiente:

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner) -> None:
        self.scanner = scanner
        self.printer = printer

    def print(self, document):
        self.printer.print(document)
    def scan(self, document):
        self.scanner.scan(document)

#De esta forma, podríamos pasar en su constructor, un objeto printer y un objeto scanner que ya
#traigan sus funciones implementadas