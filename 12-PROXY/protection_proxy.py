"""
MOTIVACION:
un proxy proporciona la misma interfaz que se estaba utilizando pero un comportamiento totalmente
diferente.

Es una clase que funciona como una interfaz para un recurso concreto. Ese recurso puede ser remoto,
costoso de construir, puede requerir logging o alguna otra funcionalidad
"""

#Protection proxy

class Car:
    def __init__(self,driver) -> None:
        self.driver = driver
    
    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


    """
    si derepente queremos poner un control de edad de 18 años, podemos ir y modificar el método
    drive, pero eso viola el principio de open closed
    """
class CarProxy:
    def __init__(self, driver) -> None:
        self.driver = driver
        self._car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print(f"Driver {self.driver.name} too young")

class Driver:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

if __name__ == "__main__":
    driver = Driver('John', 20)
    car = Car(driver)
    car.drive()
    
    driver = Driver('John', 15)
    car = CarProxy(driver)
    car.drive()

