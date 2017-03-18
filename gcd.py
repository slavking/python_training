def gcdIter(a, b):
    '''
    One easy way to do this is to begin with a test value equal to the smaller
    of the two inut arguments
    test vrednost jednaka manjoj od dva ulzna argumenta
    iteratively reduce this test value by 1 until you either reach a case
    where the test divides both a and b without remainder, or you reach 1.
    a,b: positive integers
    a,b>=0
    '''
    if (a ==0 ) or (b==0):
        print("0 is not a valid argument!")
    else:
        test = a if (a>b) else b
        while (test > 1):
            if (a % test ==0) and (b % test ==0) :
                solved = True
                break
            test-=1
        print("GCD is "+str(test))
        return test
    
def gcd(a,b):
    if (b==0):
        return a
    else:
        return gcd(b, a%b)
    

        
        

    
