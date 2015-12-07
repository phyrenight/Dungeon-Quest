import Map
import menu
def main():
	new_place = [2,3]
	dungeon = Map.Map()
	dungeon.build_level()
	dungeon.print_level()
	menu.direction_menu(new_place)
	dungeon.player_location(new_place)
	#dungeon.print_level()

if __name__ == "__main__":
	main()