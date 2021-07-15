class Creature:
    def __init__(self) -> None:
        self.strength = 10
        self.agility = 10
        self.intelligence = 10

    @property
    def sum_of_stats(self):
        return self.strength + self.agility + self.intelligence
    
    @property
    def max_stat(self):
        return max(self.strength, self.intelligence, self.agility)
    
    # @property
    # def average_stat(self):
    #     return self.sum of stats / 3.0


class Creature:
    _strength = 0
    _agility = 0
    _intelligence = 0

    def __init__(self) -> None:
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[Creature._strength]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength] = value

    @property
    def sum_of_stats(self):
        return sum(self.stats)
    
    @property
    def max_stat(self):
        return max(self.stats)
    
    @property
    def average_stat(self):
        return float(sum(self.stats)/ len(self.stats))