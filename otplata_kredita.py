'''
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
'''
'''
 The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180 

Assume that the interest is compounded monthly according to the balance
at the end of the month (after the payment for that month is made).
The monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become negative using this
payment scheme, which is okay. A summary of the required math is found below:
'''

balance=3329
annualInterestRate =0.2

def kreditno_stanje(balance,annualInterestRate,monthlyPayment):
    prevbalance=balance #previous balance
    MIR=(annualInterestRate/12.0) #monthly interest rate = MIR
    for i in range(0,12):
        MMP=monthlyPayment #minimum monthly payment =MMP
        MUB=prevbalance-MMP #monthly unpaid balance = MUB
        updatedbalance = (MUB) + (MIR*MUB)
        #print("Remaining balance"+str(round(updatedbalance,2)))
        prevbalance=updatedbalance
    return round(updatedbalance,2)

p=0

while (kreditno_stanje(balance,annualInterestRate,p) >= 0):
    p+=10
else:
    print(p)
    
