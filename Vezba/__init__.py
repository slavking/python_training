# -*- coding: utf-8 -*-
s='aasdasdasdqweeeeee1'

def vowel_count(s):
    count=0
    for symbol in s.lower():
        if symbol in set('aeiou'):
            count+=1
    return count
print("Samoglasnici s u skupu aeiou =",vowel_count(s))


"""
def vowcount(s):
				s=str()
c=0

if s in "aeiou":
	for s in "aeiou":
		c+=1
else:
		print "No vowels found!"

print "Number of vowels:",c,

ne radi - nemacki primer lel

ruskie
sum([1 for i in "sukahuipizda" if i in "aeiou"])


counter = 0
for v in "aeiou":
    for s in "huigovnopidor":
        if s==v:
          counter += 1
print counter

"""


