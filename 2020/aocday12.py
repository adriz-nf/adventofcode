from math import sin, cos, radians
with open('/Users/andrewemmett/Projects/adventofcode/2020/day12input.txt') as file:
    data = [(line.strip()) for line in file.readlines()]
commands = [(command[0],int(command[1:]) )for command in data]

class ship_og:
    "this is the first ship"
    def __init__(self, x=0, y=0, degree=0):
	    self.direction = degree
	    self.x_location = x
	    self.y_location = y

    def get_location(self):
    	return (self.x_location, self.y_location, self.direction)
    def get_manhattan(self):
    	return (abs(self.x_location) + abs(self.y_location))	
    def move(self, action, value):
        if action == 'N':
        	self.y_location += value
        elif action == 'E':
        	self.x_location += value
        elif action == 'W':
        	self.x_location -= value
        elif action == 'S':
        	self.y_location -= value
        elif action == 'L':
        	self.direction -= value
        elif action == 'R':
        	self.direction += value
        elif action == 'F':
        	self.y_location += int(cos(radians(self.direction))) * value
        	self.x_location += int(sin(radians(self.direction))) * value

class ship:
    "this ship travels by waypoints"
    def __init__(self, x=0, y=0):
	    self.x_location = x
	    self.y_location = y

    def get_location(self):
    	return (self.x_location, self.y_location, self.direction)
    def get_manhattan(self):
    	return (abs(self.x_location) + abs(self.y_location))	
    def move(self, action, value, waypoint):
        if action == 'F':
        	self.y_location += (waypoint.y_location * value)
        	self.x_location += (waypoint.x_location * value)
        else:
        	waypoint.rotate_waypoint(action, value)
        	
class waypoint:
    "this is the waypoint"
    def __init__(self, x=10, y=1):
	    self.x_location = x
	    self.y_location = y

    def get_location(self):
    	return (self.x_location, self.y_location)
    def rotate_waypoint(self, action, value):
        if action == 'N':
        	self.y_location += value
        elif action == 'E':
        	self.x_location += value
        elif action == 'W':
        	self.x_location -= value
        elif action == 'S':
        	self.y_location -= value
        elif action == 'L':
        	 self.y_location, self.x_location = 	 self.x_location * int(sin(radians(value))) + self.y_location * int(cos(radians(value))) , \
        	  									-1 * self.y_location * int(sin(radians(value))) + self.x_location * int(cos(radians(value)))
        elif action == 'R':
        	 self.y_location, self.x_location = -1 * self.x_location * int(sin(radians(value))) + self.y_location * int(cos(radians(value))), \
        	  										 self.y_location * int(sin(radians(value))) + self.x_location * int(cos(radians(value)))
        elif action == 'F':
        	print('error: F in waypoint')
        	

    
def play_instructions(ship, commands):
	for command in commands:
		#print(command)
		ship.move(command[0],command[1])
		#print(ship.get_location())
	return ship.get_manhattan()


def play_way_point_instructions(ship, waypoint, commands):
	for command in commands:
		#print(command)
		ship.move(command[0],command[1], waypoint)
		#print(ship.get_location())
	return ship.get_manhattan()

print(play_way_point_instructions(ship(0,0),waypoint(10,1), commands))


#my_ship = ship(1,1)
#print(my_ship.x_location)