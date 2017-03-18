def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    #lambda ekvivalent (sa kljucnom reci lambda) :
    #lambda x: x[0]*x[1]
    def product(A):
        return A[0]*A[1]

    K=L.copy()

    print('L '+str(K)+' '+str(s))
    m=[0 for x in L]
    print(m)
    #print(list(zip(L,m)))
    I=sum(map(product,zip(L,m)))
    print(list( map(product,zip(L,m))))
    if (I == s):
        return sum(m)
    delta=0
    for i in range(len(m)):
        while (I < s):
            m[i]+=1
            I=sum(map(product,zip(L,m)))
            print('m '+str(m)+' I '+str(I) )
            if (I == s): return sum(m)
            if (I > s): break
            
        while (I >s):
            m[i]-=1
            I=sum(map(product,zip(L,m)))
            print('m '+str(m)+' I '+str(I) )
            if (I == s): return sum(m)
            if (I < s): break
            
    return 'no solution'       
#ispravni izlazi
print(greedySum([10, 5, 1], 11))      #2
print(greedySum([10, 5, 1], 14)) #5
print(greedySum([10, 8, 5, 1], 13)) #
print(greedySum([15, 12, 4, 3, 1], 29)) #4
print(greedySum([12, 10, 8, 5, 2], 17)) #2
print( greedySum([10, 7, 6, 3], 19)) # no solution 
print(greedySum([50, 25, 5], 5)) #1
#print(greedySum([1,2,3,5,10],20))






