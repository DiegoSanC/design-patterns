from enum import Enum
from math import *
from typing import Text 


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    #Esta sería una posible solución, pero un nuevo sistema de coordenadas rompería el principio de
    # open closed. Ademas, hay que hacer una suposición sobre que "a" mapea con "x" y "b" con "y"
    # def __init__(self, a, b, system=CoordinateSystem.CARTESIAN) -> None:
    #     if system == CoordinateSystem.CARTESIAN:
    #         self.x = a
    #         self.b = b
    #     elif system == CoordinateSystem.POLAR:
    #         self.x = a * cos(b)
    #         self.y = a* sin(b)

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    @staticmethod
    def new_cartesian_pont(x,y):
        #Un factory method es cualquier método que cree un objeto. Es una alternativa
        # para inicializar objetos que tiene muchas ventajas
        return Point(x,y)
    
    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"

if __name__ == "__main__":
    p = Point(2,3)
    p2 = Point.new_polar_point(1,2)
    print(p, p2)