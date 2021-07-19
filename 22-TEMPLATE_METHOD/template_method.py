"""
El diseño basado en templates ahce lo mismo que el patrón de estrategias soo que este lo hace através de la
herencia.
-Se definen las lineas generales del algoritmo en la clase base usando metodos abstractos
-Las clases que heredan sobre escriben dichos métodos abstractos
-Se invoca al metodo template

En general los deja definir el esqueleto del algoritmo, pero las particularidades se definen en las clases que
heredan
"""
from abc import ABC

class Game(ABC):
    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.current_player = 0
    
    #Template method
    def run(self):
        self.start()
        while not self.have_winner:
            self.take_turn()
        
        print(f"Player {self.winning_player} wins!")
    
    def start(self):pass

    @property
    def have_winner(self): pass

    def take_turn(self): pass

    @property
    def winning_player(self): pass


class Chess(Game):
    def __init__(self):
        super().__init__(2)
        self.max_turn = 10
        self.turn = 1

    def run(self):
        return super().run()
    
    def start(self):
        print(f"Starting a game of chess with 2 players")
    
    @property
    def have_winner(self):
        return self.turn == self.max_turn
    
    def take_turn(self):
        print(f"Turn {self.turn} taken by player {self.current_player}")
        self.turn += 1
        self.current_player = 1- self.current_player
    
    @property
    def winning_player(self):
        return self.current_player



if __name__ == "__main__":
    chess = Chess()
    chess.run()