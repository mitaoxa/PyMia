import sys
import string

f = open('00018601.WTH', 'r')
tmp=f.readline()
words= tmp.split()
for word in words:
	print word
f.close
