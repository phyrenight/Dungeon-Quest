
def Move(direction, current_position):
	
	if direction =='n' and current_position[0] != 0:
	    current_position[0] -= 1
	
	elif direction =='e' and current_position[1] != 4:
		current_position[1] += 1
	
	elif direction == 's' and current_position[0] != 4:
		current_position[0] += 1
		
	elif direction == 'w' and current_position[1] != 0:
		current_position[1] -= 1