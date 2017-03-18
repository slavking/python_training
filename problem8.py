def f(i):
    return i + 2
def g(i):
    return i > 5


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # IN PROGRESS
    '''For example, the following functions, f, g, and test code:

    def f(i):
         return i + 2
    def g(i):
        return i > 5

    L = [0, -10, 5, 6, -4]
    print(applyF_filterG(L, f, g))
    print(L)

    Should print:

    6
    [5, 6]
'''
    count=0
    while (count < len(L)):
        if not g(f(L[count])) :
            L.pop(count)
            count=0
        else:
            count+=1
    
   
    return max(L) if len(L)>=1 else -1


L = [0,-4,3,2,1,5]
print(applyF_filterG(L, f, g))
print(L)
