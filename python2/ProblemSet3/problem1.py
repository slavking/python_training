import itertools
import bisect
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb=maxBirthProb
        self.clearProb=clearProb
        

        

    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        #weighted_choices=[(True,round(self.clearProb*100)),(False,round((1-self.clearProb))*100)]
        #population = [val for val, cnt in weighted_choices for i in range((cnt))]
        #x=random.choice(population)
        weighted_choices=[(True,self.clearProb),( False,1-self.clearProb)]
        choices, weights = zip(*weighted_choices)
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        return choices[bisect.bisect(cumdist, x)]
        #return x

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        weighted_choices=[(True,self.maxBirthProb*(1-popDensity)),(False,(1-(self.maxBirthProb*(1-popDensity) )))]
        choices, weights = zip(*weighted_choices)
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        y= choices[bisect.bisect(cumdist, x)]
        #print('length of population '+str(len(population)))
        #print(self)
        
        if y == True :
            #print('Succesfully reproduced')
            return SimpleVirus(self.maxBirthProb,self.clearProb)
        else:
            raise NoChildException



class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses=viruses.copy()
        self.maxPop=maxPop
        self.popDensity=len(viruses)/maxPop
        

        

    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxpop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """

        return len(self.viruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        for x in self.viruses:
            if x.doesClear() == True:
                self.viruses.remove(x)
        self.popDensity=len(self.viruses)/self.maxPop
        for x in self.viruses:
            try:
                y=x.reproduce(self.popDensity)
                self.viruses.append(y)
            except NoChildException:
                pass
   
        return self.getTotalPop()
