'''Hint: You might want to use bin() on an int to get a string, get rid of the first two characters,
add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.

For example,

    If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
    If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
    If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]

More specifically, write a function that meets the specifications below:
'''
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    import numpy as np
    #brute force algoritam

    def int_to_bin_list(num):
        string=bin(num)
        string=string[2:]
        L=[int(x) for x in string]
        if len(choices)-len(L) > 0:
            for x in range(len(choices)-len(L)):
                L.insert(0,0)       
        return L
    
    def product(I):
        return I[0]*I[1]

    L = [1 for x in choices]
    num=0
    for i in range(len(L)):
        num=num+(2**i)
    solutions=[]
    for x in range(num, -1 , -1):
        A=int_to_bin_list(x)
        K=sum(map(product,zip(A,choices)))
        if K <= total:
            R=A,K
            solutions.append(R)
        

    def sorting(L):
        J=sorted(L,key=lambda x:x[1],reverse=True)
        minimum=sum(J[0][0])
        minindex=0
        i=0
        while J[i][1] == total:
            if sum(J[i][0])<minimum:
                minimum=sum(J[i][0])
                minindex=i
            i+=1
        return J[minindex][0]

    O=np.array(sorting(solutions))      
    return O


print(find_combination([1,2,2,3],4))  #[1 0 0 1] ili [1 0 0 1] numpy nizovi
print(find_combination([1,1,3,5,3],5))# [ 0 0 0 1 0]
print(find_combination([1,1,1,9],4)) # [1 1 1 0]
