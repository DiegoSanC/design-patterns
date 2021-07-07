#La motivación para la creación de un bridge es prevenir la explosión de la complejidad
# del producto cartesiano

#Basicamene se trata de un mecanismo que desacopla una interfaz (jerarquía) de una implementacion

#Tenemos una acplicacion que dibuja circulos y cuadrados por pixeles o por vectores
# Una aproximacion es 4 clases: VectorCircle, VectorSquare, etc
#Este enfoque no escala si aumenta el numero de posibilidades

#cómo hacemo la conexion entre las formas y los renders => Bridge pattern

from abc import ABC

class Renderer(ABC):
    def render_circle(self, radius):
        pass

    # def render_square(self, side):
    #     pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels circle of radius {radius}")


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self):
        pass
    def resize(self, factor):
        pass

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius
    
    #En este metodo es donde realmente utiizamos el bridge
    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor

if __name__ == "__main__":
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()
    circle = Circle(raster, 5)
    circle.draw()
    circle.resize(2)
    circle.draw()

# El objetivo del bridge pattern es evitar la explosion de complejidad cuando aumentan las combinaciones
# Esto lo consigue conectando jerarquias de diferentes clases mediante un parámetro. Lo añades 
#al constructor, lo almacenas y ya tienes la conexión
