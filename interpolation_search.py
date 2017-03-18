#binarna pretraga
#binary
# binary binarna bisection search
# interpolacija interpolation


def bisection_search(L,key):
    def bisect_search_help_helper(L, key, low, high):
        #print(L)
        if high == low:
            return L[low] == key , key, low
        mid = (low + high) //2
        print (low, mid, high, key)
        if L[mid] == key:
            return True , key, mid
        elif L[mid] > key:
            if low == mid:
                return False, mid
            else:
                return bisect_search_help_helper(L, key, low, mid -1)
        else:
            return bisect_search_help_helper(L, key, mid +1, high)
        
    if len(L) == 0:
        return False
    else:
        return bisect_search_help_helper(L, key, 0 ,len(L)-1)

def interpolation_search(L,key):
    low = 0
    high = len(L) - 1
    

    while ( L[high] != L[low] and key >= L[low] and key <= L[high]):
        mid = low + ((key - L[low])*(high - low)) // (L[high] - L[low])
        #print (L)
        print (low, mid, high, key)
        if L[mid] < key :
                     low = mid + 1
        elif (L[mid] > key):
                     high = mid - 1
        else :
                     return (True, key, mid)

    if ( key == L[low] ):
                     return (True, key, low)
    else :
                     return (False, key)
                 
    
                        
X = [ x for x in range(0,501)]
#print(X)
      

A= [0,1,5,7,13,33,34,35,131,132,137,100,123,200,300,400,500,577,700,123124,454564646,444444444444]

print('interpolation')
print(interpolation_search(A,303))
print('bisection')
print(bisection_search(A,303))

print('interpolation')
print(interpolation_search(X,200))
print('bisection')
print(bisection_search(X,303))

