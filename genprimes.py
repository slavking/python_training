def genPrimes():
    prime=[]
    #yield 1 ispravno !
    prime.append(2)
    yield 2
    x=3
    while True:
        for p in prime:
            if (x%p) != 0 :
                flag = True
            else:             
                flag = False
                break;
            
        if (flag == True):
            prime.append(x)
            yield x
        x=x+1
      
               
    

prost=genPrimes()
prost.__next__()

'''
RESENJE!
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html

ako se pojavi break u for petlji, izvrsava se else blok
ako while uslov nije tacan, izvrsava se else blok

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
'''
