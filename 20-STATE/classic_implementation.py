"""
Un telefono depende del estado del telefono/linea
-Si suena lo puedes coger

Se trata de un patron donde el comportamiento de un determinado estado está determinado por su propio estado.
Hay un disparado de un estado a otro => state machine
"""

#LIGHT SWITCH

from abc import ABC

class Switch:
    def __init__(self) -> None:
        self.state = OffState()

    def on(self):
        self.state.on(self)
    
    def off(self):
        self.state.off(self)

class State(ABC):
    def on(self, switch):
        print("Light is already on")
    
    def off(self, switch):
        print("Light is already off")



class OnState(State):
    def __init__(self):
        print("Ligth turned on")
    
    def off(self, switch):
        print("Turning light off...")
        switch.state = OffState()
    
class OffState(State):
    def __init__(self) -> None:
        print("Light turned off")
    
    def on(self, switch):
        print("Turning light on...")
        switch.state = OnState()





if __name__ == "__main__":
    sw = Switch()

    sw.on()
    sw.off()
    sw.off()