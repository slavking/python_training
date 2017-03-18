import random
import pylab
import numpy

# Global Variables
##MAXRABBITPOP = 1000
##CURRENTRABBITPOP = 500
##CURRENTFOXPOP = 30
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
MAXRABBITPOP = 1000

import random
import itertools
import bisect

def chance(probability):
    weighted_choices=[(True,probability),( False,1-probability)]
    choices, weights = zip(*weighted_choices)
    cumdist = list(itertools.accumulate(weights))
    x = random.random() * cumdist[-1]
    return choices[bisect.bisect(cumdist, x)]

class Rabbit(object):
    def __init__(self):
        pass
    def new_rabbit(self,probability):
        if chance(probability):
            return True
        else:
            return False

class Fox(object):
    def __init__(self):
        self.hunted = False
    def fox_eats_rabbit(self,probability,numrabbits):
        if numrabbits>10 and chance(probability) :
            self.hunted=True
            return True
        else:
            self.hunted = False
            return False

    def fox_dies(self,pop):
        if self.hunted == False and chance(9/10) and pop>10 :
            return True
        else:
            return False

    def new_fox(self):
        if self.hunted == True and chance(1/3):
            return True
        else:
            return False
                
        
            

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    # IN PROGRESS
    rabbitlist=[]
    def reproduction(current):
        return 1.0 - current/MAXRABBITPOP
    for x in range(CURRENTRABBITPOP):
        rabbitlist.append(Rabbit())
    rabbitcopy=rabbitlist.copy()
    for rabbit in rabbitcopy:
        if rabbit.new_rabbit(reproduction(CURRENTRABBITPOP)):
            rabbitlist.append(Rabbit())
            CURRENTRABBITPOP+=1
    #if len(rabbitlist) == CURRENTRABBITPOP:
    #    print('okay! '+str(CURRENTRABBITPOP)+' rabbits')
            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # IN PROGRESS
    foxlist=[]
    def probability():
        return CURRENTRABBITPOP/MAXRABBITPOP
    
    for i in range(CURRENTFOXPOP):
        foxlist.append(Fox())
    foxcopy=foxlist.copy()
    for fox in foxcopy:
        if fox.fox_eats_rabbit(probability(),CURRENTRABBITPOP):
            CURRENTRABBITPOP-=1
            #print('Fox eats rabbit')
        if fox.fox_dies(CURRENTFOXPOP):
            CURRENTFOXPOP-=1
            #print('Fox dies')
            foxlist.remove(fox)
        if fox.new_fox():
            CURRENTFOXPOP+=1
            #print('New fox')
            foxlist.append(Fox())
    #if len(foxlist) == CURRENTFOXPOP :
    #    print(' current fox pop ='+str(CURRENTFOXPOP))
            
            
        
        
        
    
    
            
def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    # in PROGRESS

    rabbit_populations=[]
    fox_populations=[]

    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_populations.append(CURRENTRABBITPOP)
        fox_populations.append(CURRENTFOXPOP)

    #if len(rabbit_populations)==numSteps and len(fox_populations)==numSteps:
    #    print('okay')

    pylab.figure('foxes and rabbits')
    pylab.plot(rabbit_populations,label='rabbit')
    pylab.plot(fox_populations,label='fox')
    pylab.legend()

    pylab.figure('polyfit rabbit')
    coeff = numpy.polyfit(range(len(rabbit_populations)), rabbit_populations, 2)
    pylab.plot(numpy.polyval(coeff, range(len(rabbit_populations))))

    pylab.figure('polyfit fox')
    coeff = numpy.polyfit(range(len(fox_populations)), fox_populations, 2)
    pylab.plot(numpy.polyval(coeff, range(len(fox_populations))))
    
    pylab.show()
    
    return (rabbit_populations, fox_populations)

    
print(runSimulation(200))
