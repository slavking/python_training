#s="sazcbobobegghakl"
#if curr<=next
#next = current
#else nothing
#s = 'wtkprnkfnpzkhixtqcyd'# sol: fnpz got cy
#s = 'llauvyfjfyjhkekgu' #sol:auvy got ek
#s = 'tyjiokicuapyqxjqsr'# sol:apy got jqs
#s = 'nvewxjfj' #sol Longest substring in alphabetical order is: ewx
#s = 'tutnllzkmiebnwcgwqpfkbx' #sol: llz got fk
#s = 'abcdefghijklmnopqrstuvwxyz'
#*** ERROR: Expected 'abcdefghijklmnopqrstuvwxyz', got 'abcdefghijklmnopqrstuvwxy'. ***
#s = 'lcgczplcetnycirq' #sol: cet
#s = 'zyxwvutsrqponmlkjihgfedcba' #sol z
#s = 'xlyrihrpkwrruqqdjk' #sol rru
#s = 'nwckfkwrnpzmcttugh' #sol cttu
s = 'qvotwsidydfdyhqznrj'#sol nr


string=""
maxstring=s[0]
counter=0
flag=False
maxim=0
i=0
#print(len(s))


for counter in range(0,len(s)-1) :
    s1 = s[counter]
    s2=s[counter+1]
    
    if ord(s1) <= ord(s2):
        flag=True
        i+=1
        string=string+s[counter]
        if i>maxim:
            maxim=i
            maxstring=string
        #if (counter+1==len(s)-1):
        #    string=string+s[-1]
        #    maxstring=string
    elif flag==True :
        i+=1
        string=string+s[counter]
        if (i>maxim) :
            maxim=i
            maxstring=string
        string=""
        i=0
        flag=False
    else:
        i=0
        flag=False
    #print (counter,counter+1)
    #print (s1,s2)
    #print(str(flag)+"  "+string+"   "+maxstring)
        
if (flag==True) and i+1>maxim:
        i+=1
        string=string+s[counter+1]
        maxim=i
        maxstring=string  

print("Longest substring in alphabetical order is: "+maxstring)
