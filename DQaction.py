
def Move(direction, current_position):
	"""
        args: direction - contains the letter for the direction the user wanted to move to.
              current_postion - x and y for the current postion the user is at

        feat: updates the user position according to the user's input
	"""
	
	if direction =='n' and current_position[0] != 0:
	    current_position[0] -= 1
	
	elif direction =='e' and current_position[1] != 4:
		current_position[1] += 1
	
	elif direction == 's' and current_position[0] != 4:
		current_position[0] += 1
		
	elif direction == 'w' and current_position[1] != 0:
		current_position[1] -= 1