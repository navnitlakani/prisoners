import items
from player import Player
 
class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)
 
class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='n')
 
 
class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')
 
 
class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='e')
 
 
class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='w')
 
 
class ViewWeaponInventory(Action):
    """Prints the player's weapon inventory"""
    def __init__(self):
        super().__init__(method=Player.show_weapon_inventory, name='View Weapons', hotkey='v')

class AttackGun(Action):
    def __init__(self, enemy, weapon):
        super().__init__(method=Player.attack, name="Attack using Gun " + str(weapon.damage), hotkey='g', enemy=enemy, weapon=weapon)
        
class AttackStick(Action):
    def __init__(self, enemy, weapon):
        super().__init__(method=Player.attack, name="Attack using Stick " + str(weapon.damage), hotkey='s', enemy=enemy, weapon=weapon)
        
class AttackChainSaw(Action):
    def __init__(self, enemy, weapon):
        super().__init__(method=Player.attack, name="Attack using Chainsaw " + str(weapon.damage) , hotkey='c', enemy=enemy, weapon=weapon)


