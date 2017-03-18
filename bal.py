
'''
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      
# Result Your Code Should Generate Below:
Remaining balance: 31.38
'''

#balance = 42
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
def kreditno_stanje(balance,annualInterestRate,monthlyPayment):
    prevbalance=balance #previous balance
    MIR=(annualInterestRate/12.0) #monthly interest rate = MIR
    for i in range(0,12):
        MMP=monthlyPayment #minimum monthly payment =MMP
        MUB=prevbalance-MMP #monthly unpaid balance = MUB
        updatedbalance = (MUB) + (MIR*MUB)
        #print("Remaining balance"+str(round(updatedbalance,2)))
        prevbalance=updatedbalance
    print(round(updatedbalance,2))
