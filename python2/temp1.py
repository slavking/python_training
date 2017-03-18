matrix=[]

row = 3
column = 8

for x in range(0,row):
    matrix.append([0 for x in range(0,column)])

matrix[3][8]=1

def print_matrix(L):
    row = len(L)
    for x in range(row):
        print(matrix[x])

def sumhelper(matrix):
            summer=0
            for x in range(len(matrix)):
                for y in matrix[x]:
                    if y ==1: summer +=1
            return summer
import random

print(random.randint(1,255))
