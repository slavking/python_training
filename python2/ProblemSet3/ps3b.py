# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import random
import pylab



''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
##
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


    def __str__(self):
        return 'SimpleVirus ('+str(self.maxBirthProb)+','+str(self.clearProb)+')'
        

        

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
##        weighted_choices=[(True,round(self.clearProb*100)),(False,round((1-self.clearProb))*100)]
##        population = [val for val, cnt in weighted_choices for i in range((cnt))]
        weighted_choices=[(True,self.clearProb),( False,1-self.clearProb)]
        #weights=[self.clearProb,1-self.clearProb]
        choices, weights = zip(*weighted_choices)
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        return choices[bisect.bisect(cumdist, x)]
        

    
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
##        weighted_list=[(True,round(self.maxBirthProb*(1-popDensity)*100)),(False,round(100*(1-(self.maxBirthProb*(1-popDensity)))))]
##        population = [val for val, cnt in weighted_list for i in range(cnt)]
        weighted_choices=[(True,self.maxBirthProb*(1-popDensity)),(False,(1-(self.maxBirthProb*(1-popDensity) )))]
        choices, weights = zip(*weighted_choices)
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        y= choices[bisect.bisect(cumdist, x)]
        #print('length of population '+str(len(population)))
        #print(self)
        
        if y == True :
            #print(str(self)+' Succesfully reproduced')
            return SimpleVirus(self.maxBirthProb,self.clearProb)
        else:
            #print(str(self)+' Doesn\'t reproduce')
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
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        
        return len(self.viruses)

    def __str__(self):
        x='Patient \n'
        for i in self.viruses:
            x+=(str(i)+'\n')
        return x


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
        
        #print(self)
        x=0
        while x<len(self.viruses):
            if self.viruses[x].doesClear() == True:
                #print(str(self.viruses[x])+' croaks')
                self.viruses.pop(x)
            else:
                #print(str(self.viruses[x])+' doesn\'t croak')
                x+=1
        self.popDensity=len(self.viruses)/self.maxPop
        x=0
        viruscopy=self.viruses.copy()
        while x<len(viruscopy):
            try:
                y=viruscopy[x].reproduce(self.popDensity)
                self.viruses.append(y)
                x+=1
            except NoChildException:
                x+=1
        #print(self)
   
        return self.getTotalPop()

##v1=SimpleVirus(0.95,0.22)
##v1.doesClear()
##
##viruses = [
##    SimpleVirus(0.0, 0.41),
##    SimpleVirus(0.68, 0.03),
##    SimpleVirus(0.75, 0.97),
##    SimpleVirus(0.47, 0.79),
##    SimpleVirus(0.01, 0.63),
##    SimpleVirus(0.56, 0.79),
##    SimpleVirus(0.91, 0.48),
##    SimpleVirus(0.33, 0.59)
##    ]
##P1 = Patient(viruses, 9)
##P1.update()

##viruses2 = [
##    SimpleVirus(0.86, 0.8200000000000001),
##    SimpleVirus(0.83, 0.87),
##    SimpleVirus(0.13, 0.73),
##    SimpleVirus(0.57, 0.76),
##    SimpleVirus(0.23, 0.89)
##    ]
##P2 = Patient(viruses2, 7)
##print(P2.getTotalPop())
##P2.update()


#
# PROBLEM 2
#



#import random

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    
    
    timestep, values =[],[]
    for x in range(300):
        timestep.append(x)
        values.append(0)
    #print (timestep)
    #print (values)
        
    for i in range(numTrials):
        #print('trial number '+str(i))
        viruslist=[]
        for x in range(numViruses):
            #r1=random.triangular(0, maxBirthProb)
            #r2=random.triangular(0, clearProb)
            #viruslist.append(SimpleVirus(r1,r2))
            viruslist.append(SimpleVirus(maxBirthProb,clearProb))
            #print('SimpleVirus ('+str(r1)+' '+str(r2)+')')
        p=Patient(viruslist,maxPop)
        for j in range(300):
            values[j]+=p.update()
            #print('updating'+str(j)+' '+str(values[j]))
    for j in range(300):
        values[j]=values[j]/numTrials

    pylab.plot(values, label='Average')
    pylab.legend()        
        
    #pylab.ylim(0, 1000)
    #pylab.xlim(0, 300)
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Average Virus Population')
    
    pylab.show()
    return None

#print(simulationWithoutDrug(100,1000,0.1,0.05,100))
#print(simulationWithoutDrug(100,1000,random.triangular(0, 0.1),random.triangular(0, 0.05),100))
#print(simulationWithoutDrug(100,1000,0.1,0.05,100))
#print(simulationWithoutDrug(1, 10, 1.0, 0.0, 1))
#print(simulationWithoutDrug(100, 200, 0.2, 0.8, 1))
#print(simulationWithoutDrug(1, 90, 0.8, 0.1, 1))




#
# PROBLEM 3
#

#import itertools
#import bisect
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self,maxBirthProb,clearProb)
        self.resistances=resistances
        self.mutProb=mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        
        #if drug==[]:
        #    return True
        if drug in self.resistances:
           # print(drug)
           # print(self.resistances[drug])
            
            return self.resistances[drug]
        elif not drug in self.resistances: #
            return False                    #
        
        else:
            return True

    def __str__(self):
        return 'Resitant Virus ('+str(self.getMaxBirthProb())+' ' +str(self.getClearProb())+ ' '+str(self.getMutProb())+' '+str(self.getResistances())+')'


    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.maxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        def chance(random_number,weighted_list):
            choices, weights = zip(*weighted_list)
            cumdist = list(itertools.accumulate(weights))
            x=random_number*cumdist[-1]
            return choices[bisect.bisect(cumdist,x)]

        def continuation():
                weighted_choices=[(True,self.maxBirthProb*(1-popDensity)),(False,(1-(self.maxBirthProb*(1-popDensity) )))]
                mutation_list=[(True,self.mutProb),(False,1-self.mutProb)]       
                z = random.random()
                will_reproduce=chance(z,weighted_choices)
                
                will_self_mutate=chance(z,mutation_list)       
            
                new_resistances=self.resistances.copy()
                for x in self.resistances:
                    if self.resistances[x]==True and chance(random.random(),mutation_list)==True:
                        new_resistances[x]=False
                    if self.resistances[x]==False and chance(random.random(),mutation_list)==True:
                        new_resistances[x]=True
                
       
                
                if will_reproduce == True :
                    return ResistantVirus(self.maxBirthProb,self.clearProb,new_resistances,self.mutProb)
                else:
                    raise NoChildException

        if activeDrugs==[]:
            return continuation()
        else:
            for x in activeDrugs:
                if self.isResistantTo(x)==False:
                    raise NoChildException
            return continuation()


        






'''
Test: ResistantVirus 5

Test for virus reproduction with drugs applied.
s
Your output:

    virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
    Test: child = virus.reproduce(0, ["drug2"])
    Fail: virus should not reproduce.

Correct output:

    virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
    Test: child = virus.reproduce(0, ["drug2"])
    Test: child = virus.reproduce(0, ["drug1"])
    Test completed.

'''
#virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
#child=virus.reproduce(0,["drug2"]) #fail - treba exception, virus should not reproduce
#child=virus.reproduce(0,["drug1"]) #virus = ResistantVirus(1.0, 0.0, {"drug1":True, "drug2":False}, 0.0)
'''
Test: ResistantVirus 6

Check that mutProb is applied correctly in the reproduce step.

Your output:

    virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
    Reproducing 10 times by calling virus.reproduce(0, [])
    Checking the resistances of the children to each of the 6 prescriptions.
    Since mutProb = 0.5 and the parent virus was resistant to all 6 drugs, we expect each child to be resistant to, on average, half of the six drugs.
    Failed test. The children of `virus` should have varying resistances to the drugs. Here are the resistances of your sample:
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

Correct output:

    virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
    Reproducing 10 times by calling virus.reproduce(0, [])
    Checking the resistances of the children to each of the 6 prescriptions.
    Since mutProb = 0.5 and the parent virus was resistant to all 6 drugs, we expect each child to be resistant to, on average, half of the six drugs.
    Test completed.

Test: ResistantVirus 6

Check that mutProb is applied correctly in the reproduce step.

Your output:

    virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
    Reproducing 10 times by calling virus.reproduce(0, [])
    Checking the resistances of the children to each of the 6 prescriptions.
    Since mutProb = 0.5 and the parent virus was resistant to all 6 drugs, we expect each child to be resistant to, on average, half of the six drugs.
    AttributeError: 'NoneType' object has no attribute 'isResistantTo'

Correct output:

    virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
    Reproducing 10 times by calling virus.reproduce(0, [])
    Checking the resistances of the children to each of the 6 prescriptions.
    Since mutProb = 0.5 and the parent virus was resistant to all 6 drugs, we expect each child to be resistant to, on average, half of the six drugs.
    Test completed.


'''
##virus = ResistantVirus(1.0, 0.0, {'drug1':True, 'drug2': True, 'drug3': True, 'drug4': True, 'drug5': True, 'drug6': True}, 0.5)
###print(virus)
##for x in range(5):
##    child=virus.reproduce(0,[])
##    print(child)

        

            

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        self.drugs=[]
        Patient.__init__(self,viruses, maxPop)

        


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if not newDrug in self.drugs:
            self.drugs.append(newDrug)
        return None
        

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        drugset=set(drugResist)
        virusset=set()
        summ=0
        if drugResist == []:
            return len(self.viruses) 
        else: #isResistantTo
            counter=0
            for x in self.viruses:
                virusset=set(x.resistances.keys())
                #print('virusset ' +str(virusset))
                #print('drugset ' +str(drugset) )
                if drugset.issubset(virusset):
                    #print('presek '+str(drugset.intersection(virusset)))
                    L=list(drugset.intersection(virusset))
                    flag=True
                    for y in L:
                        if x.isResistantTo(y):
                            pass
                        else:
                            flag=False
                    if flag==True :
                        summ+=1
        return summ
                       


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        
        x=0
        while x<len(self.viruses):
            if self.viruses[x].doesClear() == True:
                self.viruses.pop(x)
            else:
                x+=1
        self.popDensity=len(self.viruses)/self.maxPop
        x=0
        viruscopy=self.viruses.copy()
        while x<len(viruscopy):
            try:
                y=viruscopy[x].reproduce(self.popDensity,self.drugs)
                self.viruses.append(y)
                x+=1
            except NoChildException:
                x+=1
   
        return self.getTotalPop()

'''

Test: TreatedPatient 5

Test of getting TreatedPatient's resistant pop

Your output:

    virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
    virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
    virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
    patient = sm.TreatedPatient([virus1, virus2, virus3], 100)
    patient.getResistPop(['drug1']): 2
    patient.getResistPop(['drug2']): 3
    patient.getResistPop(['drug1','drug2']): 5
    patient.getResistPop(['drug3']): 3
    patient.getResistPop(['drug1', 'drug3']): 5
    patient.getResistPop(['drug1','drug2', 'drug3']): 8
    Test completed.

Correct output:

    virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
    virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
    virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
    patient = sm.TreatedPatient([virus1, virus2, virus3], 100)
    patient.getResistPop(['drug1']): 2
    patient.getResistPop(['drug2']): 2
    patient.getResistPop(['drug1','drug2']): 1
    patient.getResistPop(['drug3']): 0
    patient.getResistPop(['drug1', 'drug3']): 0
    patient.getResistPop(['drug1','drug2', 'drug3']): 0
    Test completed.
'''
##virus1 = ResistantVirus(1.0, 0.0, {"drug1": True}, 0.0)
##virus2 = ResistantVirus(1.0, 0.0, {"drug1": False, "drug2": True}, 0.0)
##virus3 = ResistantVirus(1.0, 0.0, {"drug1": True, "drug2": True}, 0.0)
##patient = TreatedPatient([virus1, virus2, virus3], 100)
##print(patient.getResistPop(['drug1']))
##print(patient.getResistPop(['drug2']))
##print(patient.getResistPop(['drug1','drug2']))
##print(patient.getResistPop(['drug3']))
##print(patient.getResistPop(['drug1','drug3']))
##print(patient.getResistPop(['drug1','drug2','drug3']))


#
# PROBLEM 4
#

#from ps3b_precompiled_35 import *
#random.seed(0)
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    
    timestep, values,resistant =[],[],[]
    for x in range(300):
        timestep.append(x)
        values.append(0)
        resistant.append(0)

        
    for i in range(numTrials):
     
        viruslist=[]
        for k in range(numViruses):
            viruslist.append(ResistantVirus(maxBirthProb,clearProb, resistances, mutProb))
        #print(len(viruslist))
        p=TreatedPatient(viruslist,maxPop)
        #print(p.getResistPop(["guttagonol"]))
        #c=input(' aaa')
        #print('i = ',i)
        for j in range(300):
            values[j]+=p.update()
            #if j<50:
                #c=input(' aaa')
                #print(values[j])
            resistant[j]+=p.getResistPop(["guttagonol"])
            if j == 149: #trebalo je na 150om koraku, tj. koraku od 0 do 149
                p.addPrescription("guttagonol")
            
    for j in range(300):
        values[j]=values[j]/numTrials
        #print(values[j])
        resistant[j]=resistant[j]/numTrials
        #print(resistant[j])

    pylab.figure('val resist')
    pylab.plot(values, label='Virus Population')
    pylab.plot(resistant, label='Resistant Population')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time step')
    pylab.ylabel('# viruses')
    pylab.legend()    
    pylab.show()


#simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 100)

#simulationWithDrug(1, 10, 1.0, 0.0, {}, 1.0, 5)  #treba da bude 3.4 u drugom koraku umesto 3.2 i da bude 10.4

#simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5) #treba da bude 21.8 umesto 20.4

#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)

