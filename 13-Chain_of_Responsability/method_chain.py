#Motivacion:
"""
clickas a un elemento en el form => quien gestiona el click
- el boton
-el group box
-underlaying window

Esencialmente, encadenar componenetes para que todos tengan la oportunidad de 
realizar algún procesamiento. Opcionalmente con la capacidad de terminar la 
cadena
"""

class Creature:
    def __init__(self, name, attack, defense) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense
    
    def __str__(self) -> str:
        return f"{self.name} ({self.attack}/{self.defense})"

class CreatureModifier:
    def __init__(self, creature) -> None:
        self.creature = creature
        #esto va a apuntar a la siguiente funcion que se va a ejecutar
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()

class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()

class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name} defense")
            self.creature.defense += 1
        else:
            print("Not possible to increase defense")
        super().handle()

class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you")

if __name__ == "__main__":
    goblin = Creature("Gobline", 1,1)
    print(goblin)

    root = CreatureModifier(goblin)

    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.handle()
    print(goblin)

    
    root.handle()
    print(goblin)