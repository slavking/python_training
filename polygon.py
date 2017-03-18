import math

def polysum(n,s):
    perimeter =n*s
    area=0.25*n*(s**2)/math.tan(math.pi/n)
    return float("{0:.4f}".format(perimeter**2+area))
