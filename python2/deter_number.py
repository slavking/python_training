
import random
def deterministicNumber():
##    random.seed(0)
    x = random.randint(9,21)
    while not x % 2 == 0:
        x = random.randint(9,21)
    else:
        return x

##    # Possible solutions:
##
##        def deterministicNumber():
##            return 10 # or 12 or 14 or 16 or 18 or 20
##
##    # or
##    
##    def deterministicNumber():
##        random.seed(0) # This will be discussed in the video "Drunken Simulations"
##        return 2 * random.randint(5, 10)

import random
def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    x = random.randint(9,21)
    while x % 2 == 0:
        x = random.randint(9,21)
    else:
        return x

##    # Possible solutions:
##          def stochasticNumber():
##              return 2 * random.randint(5, 10)
##
##      #or 
##
##      def stochasticNumber():
##          return random.randrange(10, 22, 2)
##
##      # or, again, something like that.
        
    
