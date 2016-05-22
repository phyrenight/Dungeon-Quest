""" 
    test for dungeon quest
"""
import


def test():
	new_place = [2,3]  # players x and y coords
	dungeon = Map.Map()
	dungeon.build_level()
	dungeon.print_level()
	menu.direction_menu(new_place)
	dungeon.player_location(new_place)
	#dungeon.print_level()



if __name == "__main__":
    test()