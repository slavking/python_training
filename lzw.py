from string import ascii_lowercase



def create_initial_table(str):
    
    S=sorted(list(set(str)))
    L=[]
    table={}
    char=ascii_lowercase
    for x in char:
        if x in S:
            L.append(x)
    table_counter=0 # 0 ako kodovi pocinju od 0, 1 ako pocinju od 1
    for x in L:
        table[x]=table_counter
        table_counter+=1
    return table
    

def lzw_compression(str,tab):
    STRING=str[0]
    stringlist=[]
    table_counter=len(tab) # nista ako pocinju od 0, +1 ako kodovi pocinju od 1
    table=tab.copy()
    for i in range(1,len(str)):
        CHARACTER=str[i]
        if STRING+CHARACTER in table:
            STRING=STRING+CHARACTER
        else:
            stringlist.append(table[STRING]) #outputCode(STRING)
            table[STRING+CHARACTER]=(table_counter)
            table_counter+=1
            STRING=CHARACTER
    stringlist.append(table[STRING])        #outputCode(STRING)
    return stringlist

table = create_initial_table('babazabajabajabab')
print(table)
print('ulazni niz znakova: babazabajabajabab')
L=lzw_compression('babazabajabajabab',table)
print('izlazna lista kodova:')
print(L) #[1, 0, 4, 3, 5, 0, 2, 8, 10, 4, 1] za kodove od 0
print(len(L))
print(len(L)*4)
#[2, 1, 5, 4, 6, 1, 3, 9, 11, 5, 2] za kodove od 1
table2 = create_initial_table('pajanosijaja')
print(table2)
print('ulazni niz znakova : pajanosijaja')
L1=lzw_compression('pajanosijaja',table2)
print(L1)# [5, 0, 2, 0, 3, 4, 6, 1, 9, 9] za kodove od 0
# [6, 1, 3, 1, 4, 5, 7, 2, 10, 10] za kodove od 1
table3=create_initial_table('gattacaact')
L2=lzw_compression('gattacaact',table3)
print('\n'+str(L2) +' komprimovan string gattacaact')


def lzw_decompression(L,tab): #shadowing builting list instance

    def table_translate(code):
        R=list(table.keys())[list(table.values()).index(code)]
        #vraca kljuc po vrednosti, list.index vraca prvi indeks te vrednosti
        return R
    
    table_counter=len(tab)-1 # -1 ako kodovi pocinju od 0, nista ako pocinju od 1
    table=tab.copy() 
    
    OLD_CODE=L[0]
    CHARACTER=table_translate(OLD_CODE)
    return_string=''
    return_string+=CHARACTER
    
    for i in range(1,len(L)):
        NEW_CODE=L[i]
        #ovde je bila greska, umesto table.values() stajalo je samo table
        if not NEW_CODE in table.values(): 
            STRING=table_translate(OLD_CODE)+CHARACTER
    
        else:
            STRING=table_translate(NEW_CODE)
    
        return_string+=STRING
        
        CHARACTER=STRING[0]
        table_counter+=1
        table[table_translate(OLD_CODE)+CHARACTER]=table_counter
        
        OLD_CODE=NEW_CODE

    #print(sorted(table.items(),key=lambda x : x[1])) #sortiranje recnika po
    #vrednosti umesto po kljucu
    print('dekompresiona tabela')
    print(table)
    return return_string


print('dekomprimovana lista je sada pocetni niz znakova, bez gresaka')
string=lzw_decompression(L,table)
print(string)
print(' pocetna tabela nije izmenjena:')
print(table)

print('dekomprimovana 2 tabela')
string=lzw_decompression(L1,table2)
print(string)
print(sorted(list(table2))+(sorted(table2.values())))

D= { 'a':0, 't':1, 'm':2}
L=[0,1,3,5,2,6,4,7,2]
string=lzw_decompression(L,D)
print(string)

D={'g':0,'a':1,'t':2,'c':3}
L=[0,1,2,1,3,8,7,2]
string=lzw_decompression(L,D)
print(string)

string=lzw_decompression(L2,table3)
print(string)

