# 6.00.2x Problem Set 2: Simulating robots

import math
import random

import ps2_visualize
import pylab

# For Python 3.5:
from ps2_verify_movement35 import testRobotMovement
# If you get a "Bad magic number" ImportError, you are not using Python 3.5 


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1

random.seed(0)

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.clean_matrix=[]
        self.width=width
        self.height=height
        
        for x in range(0,self.height):
            self.clean_matrix.append([0 for x in range(0,self.width)])
        #raise NotImplementedError
    
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        
        x=math.floor(pos.getX())
        y=math.floor(pos.getY())
        #print(x)
        #print(y)
        #print (str(self.height)+' visina')
        #print (str(self.width)+' sirina')

        def print_matrix(L):
            row = len(L)
            for x in range(row):
                print(L[x])
        #print(self.clean_matrix)

        #print_matrix(self.clean_matrix)
            
        if (x>self.width) or y>self.height :
               raise ValueError
        else:
            self.clean_matrix[y][x]=1
         #   print_matrix(self.clean_matrix)
        return None
        

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (self.clean_matrix[m][n] == 1):
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        def sumhelper():
            summer=0
            for x in self.clean_matrix:
                for y in x:
                    if y ==1: summer +=1
            return summer
        return sumhelper()

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        
        #raise NotImplementedError
        x=random.uniform(0,self.width)
        y=random.uniform(0,self.height)
        return Position(x,y)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        x=pos.getX()
        y=pos.getY()
        #print(pos.getX(),pos.getY())
        #print(x,y)
        #print(self.width,self.height)
        #print(math.floor(x)==self.width)
        
        if x < 0 or y < 0 :
            return False
        if math.floor(x)==self.width or math.floor(y)==self.height:
            return False
        if math.floor(x)>=0 and math.floor(x)<= self.height and math.floor(y)>=0 and math.floor(y)<=self.width:
            return True
        
        '''
        if x < 0 or y < 0 :
            return False
        elif math.floor(x)>=0 and math.floor(x)<= self.height and math.floor(y)>=0 and math.floor(y)<=self.width:
          
            return True
        if math.floor(x)>= self.height or math.floor(y)>=self.width:
            return False
        '''

#isPositionInRoom((5.00, 5.90)) incorrectly indicates that (5.00, 5.90) is in an 5x6 room


#P=RectangularRoom(5,6)
#print(P.isPositionInRoom(Position(5.00,5.90))) #treba true
#R=RectangularRoom(10,4)
#print(P.isPositionInRoom(Position(8.55,0.70))) #treba false
#isPositionInRoom((8.55, 0.75)) incorrectly indicates that(8.55, 0.75) is in an 5x9 room
#X=RectangularRoom(3,8) #sve pozicije su u sobi
#print(P.isPositionInRoom(Position(0.64, 5.94))) #treba true 
#isPositionInRoom((3.70, 7.27)) incorrectly indicates that (3.70, 7.27) is not in an 5x10 room
#U=RectangularRoom(3,8)
#print(U.isPositionInRoom(Position(3.70, 7.27))) #treba false!
#D=RectangularRoom(5,8)
#print(D.isPositionInRoom(Position(5.00, 4.00))) #treba false



# === Problem 2
class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        #raise NotImplementedError
        self.room=room
        self.position=self.room.getRandomPosition()
        #print(self.position)
        self.room.cleanTileAtPosition(self.position)
        self.direction=random.randint(0,360)
        self.speed=speed

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        #raise NotImplementedError
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        #raise NotImplementedError
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        #raise NotImplementedError
        self.position=position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        #raise NotImplementedError
        self.direction=direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!

#U=RectangularRoom(3,8)
#R=Robot(U,300)
#print(R.getRobotDirection())
#print(R.getRobotPosition())


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #raise NotImplementedError
        
        new_position=self.position.getNewPosition(self.direction, self.speed)
        while(not self.room.isPositionInRoom(new_position)):
            self.direction=random.randint(0,360)
            new_position=self.position.getNewPosition(self.direction,self.speed)
            continue
        else:
            self.room.cleanTileAtPosition(new_position)
            self.position=new_position
            
        return self.position
        '''
        
        new_position=self.position.getNewPosition(self.direction, self.speed)
        self.position=new_position
        while (not self.
        self.room.cleanTileAtPosition(self.position)
        return self.position
               '''
'''                
R=StandardRobot(RectangularRoom(20,20),1.0)
R.setRobotDirection(90)
print(R.getRobotPosition())
R.updatePositionAndClean()
print(R.getRobotPosition())
print(R.room.getNumCleanedTiles())
R.updatePositionAndClean()
print(R.getRobotPosition())
print(R.room.getNumCleanedTiles())
R.updatePositionAndClean()
print(R.getRobotPosition())
print(R.room.getNumCleanedTiles())
R.updatePositionAndClean()
print(R.getRobotPosition())
print(R.room.getNumCleanedTiles())
R.updatePositionAndClean()
print(R.getRobotPosition())
print(R.room.getNumCleanedTiles())
'''



# Uncomment this line to see your implementation of StandardRobot in action!

#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    
    #raise NotImplementedError
    #anim = ps2_visualize.RobotVisualization(num_robots, width, height) #treba dekomentarisati
    R=RectangularRoom(width, height)
    robots=[]
    counter=num_robots
    while counter > 0:
        robots.append(robot_type(R,speed))
        counter-=1

    count=num_trials
    tick=0
    #print(R.getNumCleanedTiles()/R.getNumTiles())
    while (count > 0):
        while (R.getNumCleanedTiles()/R.getNumTiles() < min_coverage):
            for x in robots:
                x.updatePositionAndClean()
            #anim.update(R, robots) #
            #print(R.getNumCleanedTiles()/R.getNumTiles())
            tick+=1
        count-=1
        #anim.done() #
         
    
    return tick/1







# Uncomment this line to see how much your simulation takes on average
#print(runSimulation(1, 1.0, 10, 10, 0.75, 2, StandardRobot))
#avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)
#print(avg)


# === Problem 5
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #raise NotImplementedError
        self.direction=random.randint(0,360)
        new_position=self.position.getNewPosition(self.direction, self.speed)
        while(not self.room.isPositionInRoom(new_position)):
            self.direction=random.randint(0,360)
            new_position=self.position.getNewPosition(self.direction,self.speed)
            continue
        else:
            self.room.cleanTileAtPosition(new_position)
            self.position=new_position
            
        return self.position


def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print("Plotting", num_robots, "robots...")
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()

    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300//width
        print("Plotting cleaning time for a room of width:", width, "by height:", height)
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 20, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 20, RandomWalkRobot))
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    pylab.show()
    

# === Problem 6
# NOTE: If you are running the simulation, you will have to close it 
# before the plot will show up.

#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
#showPlot1('Niggardly','nigglet','niggers')

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
#showPlot2('Niggardly','nigglet','niggers') #ne radi!