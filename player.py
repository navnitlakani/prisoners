﻿import random 
import items, world
 
class Player():
    def __init__(self, name):
        self.name = name
        self.weapon_inventory = [items.Stick(), items.ChainSaw(), items.Gun()] #Inventory on startup
        self.hp = 100 # Health Points
        self.location_x, self.location_y = world.starting_position  #(0, 0)
        self.victory = False #no victory on start up

    # is_alive method
    def is_alive(self):
        return self.hp > 0   #Greater than zero value then you are still alive
 
    def show_weapon_inventory(self):
        for item in self.weapon_inventory:
            print(item, '\n')
    
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())
 
    def move_north(self):
        self.move(dx=0, dy=-1)
 
    def move_south(self):
        self.move(dx=0, dy=1)
 
    def move_east(self):
        self.move(dx=1, dy=0)
 
    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy, weapon):

        if not isinstance(weapon, items.Weapon):
            return

        enemy.attacked = True
        
        print("\nYou use {} against {}!\n".format(weapon.name, enemy.name))
        enemy.hp -= weapon.damage
        
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
            print("\nKudos!",self.name,"Won the Game\n\n")
            self.victory = True
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def do_action(self, action, **kwargs):
     action_method = getattr(self, action.method.__name__)
     if action_method:
                action_method(**kwargs)