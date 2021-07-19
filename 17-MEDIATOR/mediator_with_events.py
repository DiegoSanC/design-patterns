
class Event(list):
    """
    Un evento es basicamente una lista de funciones a las que puedes llamar cuando algo sucede
    """
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)
    
#MEDIATOR
class Game:
    def __init__(self) -> None:
        self.events = Event()

    def fire(self, args):
        self.events(args)
    
class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored) -> None:
        self.who_scored = who_scored
        self.goals_scored = goals_scored

class Player:
    def __init__(self, name, game) -> None:
        self.name =name
        self.game = game
        self.goals_scored = 0

    def score(self):
        self.goals_scored += 1
        args = GoalScoredInfo(self.name, self.goals_scored)
        self.game.fire(args)
    
class Coach:
    def __init__(self, game) -> None:
        game.events.append(self.celebrate_goal)
    
    def celebrate_goal(self, args):
        if isinstance(args, GoalScoredInfo) and args.goals_scored < 3:
            print(f"Coach says: well done, {args.who_scored}")


if __name__ == "__main__":
    game = Game()
    player = Player("Sam", game)
    coach = Coach(game)

    player.score()
    player.score()
    player.score()

"""
-Crear un mediador y tener cada objeto referenciado al mediador
-El mediador permite la comunicación bidireccional entre sus componentes conectados
-Los mediator tienen funciones a las que los componentes pueden llamar
-Los componentes tienen funciones que pueden ser llamadas por el mediator
-Hay bibliotecas de procesado de eventos (Rx) que hace la comunicación más simple de implementar
"""