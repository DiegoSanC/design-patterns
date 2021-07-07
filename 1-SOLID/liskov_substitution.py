class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._height * self._width
    
    def __str__(self):
        return f"Width: {self._width}, height: {self.height}"

    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size) -> None:
        #super().__init__(size, size) estaq opcion es valida
        Rectangle.__init__(self, size, size)

    #Estos setters tambien violan el principio de sustitucion de liskov
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
    
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

#Esta funcion rompe el principio de liskov porque solo vale para rectangulos 
# y no valdría para square que es un heredero de rectangle
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w *10)
    print(f"Expected an area of {expected}, got {rc.area}")

rc = Rectangle(2,3)
use_it(rc)
sq = Square(5)
use_it(sq)