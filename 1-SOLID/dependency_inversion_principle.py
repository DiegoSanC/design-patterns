#Clases o módulos de alto nivel no deben depender diractmente de modulos de bajo nivel.
# Deben depender de abstracciones => abstrac class o clases con métodos abstractos
# Debes depender de interfaces en lugar de depender de implementaciones concretas

from abc import abstractmethod
from enum import Enum

class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Relationships:
    def __init__(self) -> None:
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

#Desde Research, que es un high level module, estamos accediendo a la forma de almacenar de
#Relationships, que es un low level module (mete valores en una lista). si cambiamos el modo en el que
#almacena la información este modulo de bajo nivel, cualquier clase que lo usase dejaría de funcionar

#Una opcion es que el metodo de research pertenezca a la clase Relationships



class Research:
    def __init__(self, relationships) -> None:
        relations = relationships.relations
        for r in relations:
            if r[0].name == "John" and r[1] == Relationship.PARENT:
                print(f"John has a child called {r[2].name}")


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)


#Otra opción es implementar una interfaz

class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name): pass

class Relationships2(RelationshipBrowser):
    def __init__(self) -> None:
        self.relations = []
    
    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    #Si modificamo como almacenamos la info, solo tenemos que cambiar este método
    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name

class Research:
    def __init__(self, browser) -> None:
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")

parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships2 = Relationships2()
relationships2.add_parent_and_child(parent, child1)
relationships2.add_parent_and_child(parent, child2)

Research(relationships2)
