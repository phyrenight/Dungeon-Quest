class Map(object):
	size = 6
	floor_map = []


	def __init__(self):
		"""
		   Will be used when creating dungeons
		"""
		pass
	

	def build_level(self):
		"""
            builds the floor map
		"""
		for rows  in range(self.size - 1):
			self.floor_map.append(["O"]*(self.size-1))
	
	
	def print_level(self):
		"""
            prints the floor to the screen
		"""
		for row in self.floor_map:
			print "".join(row)
	
	
	def player_location(self, new_place):
		"""
		    args: new_place - list[]
		                       holds the current x and y coords of the player
		    
		    feat: used to update map to include the users new position 
		          while deleting the user old position. 
		"""
		row = 0	
		while row < 5:
			col = 0
			print row
			while col < 5:
				if (new_place[0] == row and new_place[1] == col):
				    self.floor_map[row][col] = 'X'
				else:
					self.floor_map[row][col] = 'O'
				col += 1
			row += 1
		self.print_level()
				