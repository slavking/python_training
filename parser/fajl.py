#import sys
from BeautifulSoup import BeautifulSoup
#for   t in   BeautifulSoup(sys.stdin):
    #mrtva dvotacka
for t in BeautifulSoup(open("tweets.txt")).findAll('p'):
      print (t.text)




