"""
Un proxy que parece el objeto completo que enmascara, pero realmente no  
"""
class Bitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        print(f"Loading image from {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")
    

"""
Que sucede si creamos la imagen pero no la dibujamos? Quiza el proceso de crearla es muy costoso
y solo queremos permitir hacerlo si se va a llamar a draw y si no, no dejamos.
Podríamos modificar la clase Bitmap para que solo crease la imagen cuano se fuera a dibujar,
pero eso rompería el open close principle. Además, imaginemos que Bitmap es una clase muy compleja
que es mejor no tocar porque no sabemos muy bien como funciona.
"""

class LazyBitmap:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._bitmap = None
    
    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()
        


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")

if __name__ == "__main__":
    #bmp = Bitmap("facepalm.jpg")
    #draw_image(bmp)

    bmp = LazyBitmap("facepalm.jpg")
    draw_image(bmp)
    #El proxy virtual protege de dos lecturas consecutivas, que puede suponer una operacion costosa

    draw_image(bmp)


    """
    Diferencias entre proxy y decorador:
    Un proxy proporciona una interfaz idéntica; un decorador proporciona una mejorada con operaciones
    adicionales

    Un decorador generalmente agrega o tiene una referencia a la clase que está decorando. Generalmente,
    incluye dicho objeto en el constructor del propio decorador.Un proxy no hace esto.

    De hecho, un proxy ni si quiera tiene que trabajar con un objeto materializado. Por ejemplo,
    puede hacer una construcción lazy y no volver a interactuar con el objeto creado

    """