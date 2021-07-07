#Cuando tienes muchos factory methods en una clase, surge la necesidad de agruparlos en una entidad
from enum import Enum
from math import *
from typing import Text 


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}"


#Esta clase se puede hacer como una inner class de la clase Point
class PointFactory:
    def new_cartesian_pont(self, x,y):
        p = Point()
        p.x = x
        p.y = y
        return p
    def new_polar_point(self, rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

if __name__ == "__main__":
    p = Point(2,3)
    p2 = PointFactory.new_polar_point(1,2)
    print(p, p2)