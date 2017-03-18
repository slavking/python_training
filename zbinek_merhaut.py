"""
MITx: 6.00.1x Introduction to Computer Science and Programming Using Python
2016, Week 2, polysum, Peer Assesment
Programmed by Zbynek Merhaut, email@zbynekmerhaut.cz
"""

# Import modules
import math


def polysum(n, s):
    """
    The function takes 2 arguments, 'n' and 's'. This function sum
    the area and square of the perimeter of the regular polygon.
    The function returns the sum, rounded to 4 decimal places.
    The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    The perimeter of a polygon is: n*s
    """

    area = (0.25*n*s**2) / math.tan(math.pi/n)
    perimeter = n * s
    return round(area + perimeter**2, 4)

