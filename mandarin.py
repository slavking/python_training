#mandarinski jezik

trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

privrem={'0':'zero', '1':'one', '2':'two', '3':'three', '4': 'four',
          '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '10': 'ten'}


'''example


    convert_to_mandarin('36') will return san shi liu
    convert_to_mandarin('20') will return er shi
    convert_to_mandarin('16') will return shi liu
'''

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99 
    returns the string mandarin representation of us_num
    '''
    #IN PROGRESS
    #STRING!
    if (int(us_num) < 11) :
        return trans[us_num]

    elif (int(us_num) >10 and int(us_num) <20):
        return trans['10']+' '+trans[us_num[-1]]
    else:
        return trans[us_num[0]]+' '+trans['10']+' '+trans[us_num[-1]]  \
               if us_num[-1] != '0' else trans[us_num[0]]+' '+trans['10']
