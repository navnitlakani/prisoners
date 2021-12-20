import world
from player import Player

def play():
    playerName = input("\nEnter Player Nam: ")
    print("\nWelcome to the Prison")
    print("Your mission is to kill right criminal who did crime.")
    print("\n+++++ Choose Game Level +++++\n")
    print("1) Survival")
    print("2) Killer Moves")
    level = input("Choose Game Level: ")
    world.load_tiles(level)
    player = Player(playerName)

    if level  == '1':
        print("\nYou choose Survival level.")
    else:  
        print("\nYou choose Killer Moves level.")

    #These lines load the starting room and display the text
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    print("\nChoose an move where you want to go:\n")

    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            available_weapons = room.available_weapons()
            for action in available_weapons:
                print(action)
            action_input = input('Action: ')
            for action in available_weapons:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break


if __name__ == "__main__":
    play()