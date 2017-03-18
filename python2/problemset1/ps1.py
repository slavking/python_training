###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # IN PROGRESS
    import operator
    
    vals=sorted(cows.items(),key=operator.itemgetter(1),reverse=True)

    result=[]
    trip=[]
    tripCost=0
    #for i in vals:
     #   print(i)

    def isEqual(trip):
        i=0
        while ( i < len(vals)) :
            if (tripCost + vals[i][1]) == limit:
                trip.append(vals[i][0])
                vals.pop(i)
                #print(trip)
                return (True,trip)
            else:
                i+=1
        return (False,[])

    def isLess(tripCost,trip):
        i = 0
        flag=False
       # print(trip)
        while i < len(vals) :
            #for x in vals:
            #    print(x)
                
            if (tripCost+vals[i][1])< limit:
                trip.append(vals[i][0])
                tripCost+=vals[i][1]
                vals.pop(i);
                i=0
                flag=True
            elif (tripCost + vals[i][1]) > limit:
                i=i+1
            else: 
                trip.append(vals[i][0])
                vals.pop(i)
                flag=True
                return (flag, trip)
                

            
                
        return (flag,trip)
    
    #for i in vals:
   #     print(i)
    while (vals != []):
        
        trip.append(vals[0][0])
        tripCost=vals[0][1]
        vals.pop(0)
        (boo, trip1)= isEqual(trip.copy())
        #print(str(boo)+' isEqual')
        if boo == True:
            result.append(trip1)
            trip=[]
            continue
        else:
            (boo2,trip2)=isLess(tripCost,trip.copy())
            
            #print(str(boo2)+' isLess')
            if boo2==True:
                result.append(trip2)
                trip=[]
                continue
            else:
                result.append(trip)
                trip=[]
                continue

    return result
 
    '''def greedy_cow_transport(cows,limit):
    import operator
    
    vals=sorted(cows.items(),key=operator.itemgetter(1),reverse=True)

    result=[]
    trip=[]
    tripCost=0
    #for i in vals:
        #print(i)
    for i in vals:
        if (tripCost + i[1]) <= limit:
            tripCost+=i[1]
            trip.append(i[0])
            #print('('+str(i[0]+' '+str(i[1])+') '+str(trip)+' '+str(tripCost)))#+' '+str(result)))
            
        else:
            result.append(trip)
            trip=[i[0]]
            tripCost=i[1]
    else:
        result.append(trip)
    

    return result
    '''
    
    


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    #IN PROGRESS

     
    '''    
    from pprint import pprint as pp
    from itertools import chain, combinations
 
    def powerset(iterable):
        "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    '''
    import operator

    
    vals=sorted(cows.items(),key=operator.itemgetter(1),reverse=True)

    slack_spaces=[]
    
    def perfectFit(limit,part):
        flag=True
        i=0
        slack=0
        slack_spaces=[]
        while (i<len(part)):
            L=[x[1] for x in part[i]]
            #print(L)
           # print(sum(L))
            if sum(L)<=limit:
                slack+=(limit-sum(L))
                #print(slack)
                #print('Pass')
            else:
               # print('Fail')
                flag=False
            i+=1

        
        if flag == True :
            slack_spaces.append(slack)
            #print('Total pass')
        #else:
            #print('Total fail')
        if slack_spaces != []:
            return (max(slack_spaces))
        else:
            return('Fail')


    candidate=[]

    for partitions in get_partitions(vals):
       # c=input('enter')
        #print('\n')
        #print(partitions)
        slack=perfectFit(limit,partitions)
        #print(str(partitions)+' slack='+str(slack))
        if slack != 'Fail':
            candidate.append((slack,partitions))

    #for x in candidate:
    #    print(x)
    
    def minimals(L):
        minimal=L[0][0]
        indmin=0
        listmin=[]
        for x in L:
            if x[0] <= minimal:
                minimal=x[0]
                listmin.append(x[1])
        #print(minimal)
        return listmin

    L=minimals(candidate)
    #for x in L:
        #print(x)
    D=[]
    R=[]
    for x in L:
        D=[]
        for z in x:
            trip=[r[0] for r in z]
            #print(trip)
            D.append(trip)
        R.append(D)    

    return R[0]
    

   
    
    
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))

#print(brute_force_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5},10))

print(brute_force_cow_transport({'Lotus': 40, 'Milkshake': 40, 'MooMoo': 50, 'Horns': 25, 'Miss Bella': 25, 'Boo': 20}, 100))
