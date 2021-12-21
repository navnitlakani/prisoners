import items, prisoners, weapons, world
 
class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
 
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move weapons for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(weapons.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(weapons.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(weapons.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(weapons.MoveSouth())
        return moves
 
    def available_weapons(self):
        """Returns all of the available weapons in this room."""
        moves = self.adjacent_moves()
        moves.append(weapons.ViewWeaponInventory())
 
        return moves


class StartingRoom(MapTile):
    # override the intro_text method in the superclass
    def intro_text(self):
        return """
We have 4 criminal and you need to select right criminal after choosing clue which they already have.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
    
class PrsionRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
 
    def modify_player(self, the_player):
        
        if not self.enemy.isAttacked():
            print("Criminal have 2 clues. Choose right clue to select criminal. If you choose wrong clue you will die.")  
            print("\n1) Sports")  
            print("2) Politics")  
            inp = input("\nEnter the clue: ") 
            
            if inp  == '1':
                
                return
            
            else:
                the_player.hp = 0   
                print("\nYou choose wrong clue. Player",the_player.name,"Died. Game Over!\n")   
        

    def available_weapons(self):
        if self.enemy.is_alive():
            print("\nYou choose right criminal. Now choose weapon to kill criminal:\n")
            return [
                weapons.AttackGun(enemy=self.enemy, weapon=items.Gun()),
                weapons.AttackStick(enemy=self.enemy, weapon=items.Stick()),
                weapons.AttackChainSaw(enemy=self.enemy, weapon=items.ChainSaw())
            ]
        else:
            return self.adjacent_moves()

class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another unremarkable part of the cave. You must forge onwards.
        """
 
    def modify_player(self, player):
        #Room has no action on player
        pass
 
class PrsionRoom1(PrsionRoom):
    def __init__(self, x, y):
        super().__init__(x, y, prisoners.Prisoner1())
 
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You are in prison room 1.
            """
        else:
            return """
            PrsionRoom1 dead
            """
class PrsionRoom2(PrsionRoom):
    def __init__(self, x, y):
        super().__init__(x, y, prisoners.Prisoner2())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
            You are in prison room 2.
             """
        else:
            return """
             PrsionRoom2 dead
             """
    def modify_player(self, the_player):
        
        if not self.enemy.isAttacked():
            print("Criminal have 2 clues. Choose right clue to select criminal. If you choose wrong clue you will die.")  
            print("\n1) Sports")  
            print("2) Politics")  
            inp = input("\nEnter the clue: ") 
            
            if inp  == '2':
                
                return
            
            else:
                the_player.hp = 0   
                print("\nYou choose wrong clue. Player",the_player.name,"Died. Game Over!\n")   

class PrsionRoom3(PrsionRoom):
    def __init__(self, x, y):
        super().__init__(x, y, prisoners.Prisoner2())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             You are in prison room 3.
             """
        else:
            return """
             PrsionRoom3 alive
             """


class PrsionRoom4(PrsionRoom):
    def __init__(self, x, y):
        super().__init__(x, y, prisoners.Prisoner2())

    def intro_text(self):
        if self.enemy.is_alive():
            return """
             You are in prison room 4.
             """
        else:
            return """
             PrsionRoom4 alive
             """
    def modify_player(self, the_player):
        
        if not self.enemy.isAttacked():
            print("Criminal have  2 clues. Choose right clue to select criminal. If you choose wrong clue you will die.")  
            print("\n1) Sports")  
            print("2) Politics")  
            inp = input("\nEnter the clue: ")  
            
            if inp  == '2':
                
                return
            
            else:
                the_player.hp = 0   
                print("\nYou choose wrong clue. Player",the_player.name,"Died. Game Over!\n")  
                