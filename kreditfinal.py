'''
   Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09
'''


def calc(balance,annualInterestRate):
    
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

    low=balance/12
    hi=kreditno_stanje(balance,annualInterestRate,0)
    guess=(low+hi)/2
    print("low ",low)
    print("hi ",hi)
    print("guess ",guess)
    epsilon=0.01
    initial=kreditno_stanje(balance, annualInterestRate, guess)
    while abs(initial)>=epsilon:
        if (initial) < 0:
            hi=guess
        else:
            low=guess
        guess=(hi+low)/2
        print("guess", guess)
        initial=kreditno_stanje(balance, annualInterestRate,guess)
        
    return round(guess,2)



