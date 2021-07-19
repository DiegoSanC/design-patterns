"""
 Necesitas definar una operacion en toda una herencia entre clases
 - Por ejemplo hacer que un documento sea printable en HTML/Markdown
 No queremos modificar toda la jerarquia

Necesitamos acceso a los aspectos no comunes entre la jerarquia
Creamos un componente externo que permita gestionar todo el renderizado
    -Intentando evitar type checks

Basicamente es un componente que sabe como viajar por una estructura de datos compuesta por tipos
prbablemente relacionados

"""
from enum import Enum

class DoubleExpression:
    def __init__(self, value) -> None:
        self.value = value
    
    def print(self, buffer):
        buffer.append(str(self.value))

class AdditionExpression:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
    
    def print(self, buffer):
        buffer.append('(')
        self.left.print(buffer)
        buffer.append('+')
        self.right.print(buffer)
        buffer.append(')')


if __name__ == "__main__":
    # 1 + (2+3)
    e = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )
    #En el enfoque intrusivo modificamos las clases ya construidas