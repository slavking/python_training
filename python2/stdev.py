def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    import math
    if L == []:
        return float('NaN')
    mu = 0
    N=len(L)
    for x in L:
        mu+=len(x)
    mu=mu/N
    stdev = 0
    for x in L:
        stdev+=(len(x)-mu)**2
    stdev=math.sqrt(stdev/len(L))
    return round(stdev,4)

print(stdDevOfLengths(['a','z','p']))
print(stdDevOfLengths(L = ['apples', 'oranges', 'kiwis', 'pineapples']))
'''
def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if (len(L) == 0):
        return float('NaN')
    
    # compute mean first
    sumVals = 0
    for s in L:
        sumVals += len(s)
    meanVals = sumVals / len(L)

    # compute variance (average squared deviation from mean)
    sumDevSquared = 0
    for s in L:
        sumDevSquared += (len(s) - meanVals)**2
    variance = sumDevSquared / len(L)

    # standard deviation is the square root of the variance
    stdDev = variance**(.5)

    return stdDev

# using listcomps
def stdDevOfLengths(L):
    n = len(L)
    if (n == 0):
        return float('NaN')
    lengths    = [len(s) for s in L]
    mean       = sum(lengths) / n
    squaredDev = [(l-mean)**2 for l in lengths]
    variance   = sum(squaredDev) / n    
    return variance**(.5)


# using a separate function for std dev
def stdDev(X):
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def stdDevOfLengths(L):
    n = len(L)
    if (n == 0):
        return float('NaN')
    X = []
    for s in L:
        X.append(len(s))
    return stdDev(X)
    '''
def mean(L):
    return sum(L)/len(L)

def coeff_of_variation(L):
    mu=mean(L)
    N=len(L)
    total=0
    for x in L:
        total+=(x-mu)**2
    total = (total/N)**(0.5)
    return total/mu
        
print(mean([10, 4, 12, 15, 20, 5]))

print(coeff_of_variation([10, 4, 12, 15, 20, 5]))
