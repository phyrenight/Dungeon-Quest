import Map

def direction_menu(current_position):

# comment current_postition should contain 4 values the row and column the #player is currently in and the length of the rows and columns in floor_map

    if current_position[0] == 0 and current_position[1] == 0:
        print "Go (E)ast"
        print "Go (S)outh"

    if current_position[0] == 0 and current_position[1] == 4:
        print "Go (S)outh"
        print "Go (W)est"

    if current_position[0] == 4 and current_position[1] == 4:
        print "Go (N)orth"
        print "Go (W)est"
		
    if current_position[0] == 4 and current_position[1] == 0:
        print "Go (N)orth"
        print "Go (E)ast"
			
    if current_position[0] == 0:
        print "Go (E)ast"
        print "Go (S)outh"
        print "Go (W)est"
		
    if current_position[0] == 4:
        print "Go (N)orth"
        print "Go (E)ast"
        print "Go (W)est"
		
    if current_position[1] == 0:
        print "Go (N)orth"
        print "Go (E)ast"
        print "Go (S)outh"
		
		
    if current_position[1] == 4:
        print "Go (N)orth"
        print "Go (S)outh"
        print "Go (W)est"
		
    else: 
        print "Go (N)orth"
        print "Go (E)ast"
        print "Go (S)outh"
        print "Go (W)est"