class Prisoner:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.attacked  = False
 
    def is_alive(self):
        return self.hp > 0
    
    def isAttacked(self):
        return self.attacked
 
class Prisoner1(Prisoner):
    def __init__(self):
        super().__init__(name="Prisoner1", hp=100)
 
class Prisoner3(Prisoner):
    def __init__(self):
        super().__init__(name="Prisoner3", hp=100)

class Prisoner4(Prisoner):
    def __init__(self):
        super().__init__(name="Prisoner4", hp=100)

class Prisoner2(Prisoner):
    def __init__(self):
        super().__init__(name="Prisoner2", hp=100)