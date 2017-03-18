counter=0
string=""
maximum=0

s = 'yjcizxnphifuwa' #najduzi alfabetski podniz je ciz
for i in range(0,len(s)-1):
    print(i)
    print(ord(s[i]))
    if ord(s[i])<=ord(s[i+1]) and ord(s[i-1]) >= ord(s[i]) :
        counter+=1
        string=string+s[i:i+1]
        if counter>maximum:
            maximum=counter
            maxstring=string

    else:
        counter=0
        string=""
print(maximum)
print(maxstring)
