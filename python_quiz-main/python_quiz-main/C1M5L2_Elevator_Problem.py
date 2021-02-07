'''The code below defines an Elevator class. The elevator has a current floor, 
  it also has a top and a bottom floor that are the minimum and maximum floors it can go to. 
  Fill in the blanks to make the elevator go through the floors requested.
'''

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def __str__(self):
        return ("Current floor: " + str(self.current))
        
    def up(self):
        """Makes the elevator go up one floor."""
        if(self):   
            if self.current < self.top:   # or if (self.current < 10):
                self.current += 1
        
    def down(self):
        """Makes the elevator go down one floor."""
        if(self):
            if self.current > self.bottom:  # or if (self.current > -1):
                self.current -= 1
        
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        

elevator = Elevator(-1, 10, 0)
print(elevator)

'''
    OUTPUT:
Current floor: 0

'''
elevator.up() 
elevator.current #should output 1

elevator.down() 
elevator.current #should output 0

elevator.go_to(10) 
elevator.current #should output 10

elevator.go_to(10) 
elevator.current #should output 10

'''
    OUTPUT:
9
1

'''

elevator.go_to(5)
print(elevator)

''' OUTPUT:
Current floor: 5
'''
