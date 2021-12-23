# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
      
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\n".format(self.name, self.description)

class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)
 
    def __str__(self):
        return "{}\n=====\n{}\nDamage: {}".format(self.name, self.description, self.damage)
 
class Gun(Weapon):
    def __init__(self):
        super().__init__(name="Gun",
                         description="You can use Gun to kill criminal and the damage is 50, so you need to assault 2 times",
                         damage=50)
 
class Stick(Weapon):
    def __init__(self):
        super().__init__(name="Stick",
                         description="You can use Stick to kill criminal and the damage is 10, so you need to assault 10 times.",
                         damage=10)
class ChainSaw(Weapon):
    def __init__(self):
        super().__init__(name="ChainSaw",
                         description="You can use ChainSaw to kill criminal and the damage is 100, so you need to assault only 1 time.",
                         damage=100)