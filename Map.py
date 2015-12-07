class Map():
	floor_map = []
	def __init__(self):
		pass
	def build_level(self):
		for rows  in range(6):
			self.floor_map.append(["O"]*5)
	
	def print_level(self):
		for row in self.floor_map:
			print "".join(row)
	
	def player_location(self, new_place):
		row = 0	
		while row < 5:
			col = 0
			while col < 5:
				if (new_place[0] == row and new_place[1] == col):
				    self.floor_map[row][col] = 'X'
				col += 1
			row += 1
		self.print_level()
				