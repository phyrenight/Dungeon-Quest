import Map
import menu
from DQaction import Move

def main():
    choice  = ""
    dungeon = []
    position = [1,1]
    dungeon.append(Map.Map())
    dungeon[0].build_level()
    while choice != 'quit':
        dungeon[0].player_location(position)
        print position[0], position[1]
        menu.direction_menu(position)
        print "enter quit then ENTER to exit"
        choice = raw_input("> ")
        Move(choice, position)






if __name__ == "__main__":
	main()