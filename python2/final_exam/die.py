import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # IN PROGRESS
    pylab.hist(values, bins = numBins)
    if title != None:
        pylab.title(title)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    pylab.show()

#print(makeHistogram([10,20,30,40,100,500,1000],5,'x','y','naslov'))
    
                  
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    # IN PROGRESS
    def longest_run(L):
        count=1
        #num=0

        maxCount=0
        if len(L)==1 :
            return 1
        for i in range(len(L)-1):
            if L[i+1] == L[i]:
                count +=1
                
            else:
                count =1
               
            if maxCount<count:
                maxCount=count
                #num=L[i]
        return maxCount#,num
     
    #print(longest_run([1,4,3]))
    #print(longest_run([1 ,3, 3, 2]))
    #print(longest_run([5 ,4 ,4 ,4 ,5 ,5 ,2 ,5]))
    runs=[]
    run=[]
    for i in range(numTrials):
        runs=[]
        for j in range(numRolls):
            runs.append(die.roll())
        longest=longest_run(runs)
        run.append(longest)
        
    #print(run)
    mean,std=getMeanAndStd(run)
    makeHistogram(run,10,'xLabel','yLabel')
    return mean
            
    
    
# One test case
#print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000)) #5.312
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))
