#L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
#longest monotonically increasing run = [3, 4, 5, 7, 7]
#longest monot. decreasing run = [10,4,3]
# return 26 - suma 7+7+5+4+3

#L=[5,4,10], long. increasing = [4,10], decreasing = [5,4]
#sum u oba slucaja 9, ali se uzima prvi run jer je prvi po redosledu

L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
#L=[5,4,10]
#L=[5,4]

'''
    def cleanup(inc,dec,longest):
        leni=len(inc)
        lend=len(dec)
        long=len(longest)
        if 

    def isIncreasing(L,i,inc):
         if L[i+1]>=L[i]:
             inc.append(L[i])
             inc.append(L[i+1])
          return inc
            

        
    def isDecreasing(L,i,dec):
        if L[i+1]<=L[i]:
            dec.append(L[i])
            dec.append(L[i+1])

    i=0

        
    prevInc=True
    prevDec=True
    
    
    while i< len(L)-1:
        
        if isIncreasing(L,i) and isIncreasing(L,i+1):
            temp.append(L[i])
            temp.append(L[i+1])
            tmp=cleanup(temp,longest,i)
            temp=tmp[0]
            longest=tmp[1]
            print('increasing+'+str(temp)+' '+str(longest))
            
        elif isDecreasing(L,i) and isDecreasing(L,i+1):
            temp.append(L[i])
            temp.append(L[i+1])
            tmp=cleanup(temp,longest,i)
            temp=tmp[0]
            longest=tmp[1]
            print('decreasing+'+str(temp)+' '+str(longest))
            
        elif isIncreasing(L,i) and isDecreasing(L,i+1):
            tmp=cleanup(temp,longest,i)
            temp=[L[i],L[i+1]]
            longest=tmp[1]
            print('increasing prev dec +'+str(temp)+' '+str(longest))
            
        elif isDecreasing(L,i) and isIncreasing(L,i):
            prevInc=False
            prevDec=True
            tmp=cleanup(temp,longest,i)
            temp=[L[i],L[i+1]]
            longest=tmp[1]
            print('decreasing prev inc+'+str(temp)+' '+str(longest))
            
        else:
            print('Error!') #also except('error!')
        i+=1
    '''
    

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    #IN PROGRESS
    #MONOTONO NEOPADAJUCI = monotonically increasing
    #MONOTONO NERASTUCI = monotonically decreasing
    #ASSERT at least 2 elements
    #PATIENCE SORTING - Sortiranje po pasijansu
    #primer rastuce 
    #stvaraju se gomile karata, ako odgovara uslovu .append na taj niz
    #python - stvori se novi objekat 

    from collections import namedtuple
    from functools import total_ordering
    from bisect import bisect_left
    from bisect import bisect
    
    if len(L)==2:
        return L[0]+L[1]
    
    class Node(namedtuple('Node_', 'val back')):
        def __iter__(self):  #ITER, nije init!
            while self is not None:
                yield self.val
                self=self.back
        def __lt__(self, other):
            return self.val < other.val
        def __eq__(self,other):
            return self.val == other.val

##bisect_left(list, item[, lo[, hi]])
#Locate the proper insertion point for item in list
#to maintain sorted order.

        #lo i hi su tu ako je potreban podskup liste
#sece listu piletops, ako nadje

        #od poslednjeg piletops pravi listu i vraca
#slice [::-1] - vraca listu u kontraporetku
#a[start:end:step]
# K=[3,4,5]
# F=K[::-1]
# print(F) => [5,4,3]
    #for i in pileTops:
     #   print(i)
    

    if not L:
        return []
    pileTops = []
    for di in L:
        j = bisect_left(pileTops, Node(di,None))
        print(j)
        new_node = Node(di, pileTops[j-1] if j>0 else None)
        print (new_node)
        if j== len(pileTops):
            pileTops.append(new_node)
        else:
            pileTops[j]=new_node

        print('pileTops')
        for i in pileTops:
            print(i)
            
        c=input("enter pause")
        

    increasing=list(pileTops[-1])[::-1]
    #print(increasing)
    '''
    pileTops=[]
    for di in L:
        j=bisect_left(pileTops, Node(di, None))
        #print(j)
        new_node=Node(di,pileTops[j-1] if j==0 else None)
        #print(new_node)

        if j==len(pileTops):
            pileTops.append(new_node)
        else:
            pileTops[j]=new_node

    decreasing=list(pileTops[-1])[::-1]
    #print(decreasing)

    if len(increasing)>len(decreasing) :
        return increasing
    else:
        return decreasing
   '''
    return increasing 
    
            

print(longest_run(L))
        
            
            
            

    
            
            
        
        

    
