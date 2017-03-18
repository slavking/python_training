def closest_power(base,num):
       
    
    
    exponent=0
    while abs(base**exponent-num)>=base:         # or abs(initial)>=abs(num+base):
                 
        if base**exponent > num+base:
            break
        if base>num:
            exponent =0
            break
        exponent+=1

        
    if (exponent ==0):
        return exponent
    elif abs(base**(exponent-1) - num) <= abs(base**exponent - num):         
        return round(exponent-1)
    else:
        return round(exponent)
    
'''stari
def closest_power(base,num):
    import math    
    exponent=0
    while abs(base**exponent-num)>=base:
        exponent+=0.01
    return math.floor(exponent)
'''

print(closest_power(4, 62)) #3
print(closest_power(4, 12) )#2
print(closest_power(5, 22) )#2
print(closest_power(9, 75))#2
print(closest_power(4, 160.0)) #3
print(closest_power(4, 1)) #0
print(closest_power(33, 1)) #0
print(closest_power(82, 1) )  #0  
print(closest_power(20, 210.0) ) #1   
print(closest_power(16, 136.0))#1
print(closest_power(15, 8.0)  )#0
print(closest_power(10, 550.0)) #2
print(closest_power(7, 196.0)) #2
print(closest_power(2, 384.0) )#8
print(closest_power(4, 160.0)) #3
