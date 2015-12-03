#!/usr/bin/env python
import sys
import re
MAX_RECURSION = 1000
sys.setrecursionlimit(MAX_RECURSION)

def usage():
  print "Usage: %s [seq_number]\n\tseq_number should be between 2 and %s" % (sys.argv[0], MAX_RECURSION - 2)
  exit(1)

if( len(sys.argv) < 2 or int(sys.argv[1]) < 2 or int(sys.argv[1]) > MAX_RECURSION - 2 ):
  usage()

i = 0
fibolist = []

def fibonacci(x,y):
  global i
  global fibolist
  i += 1 
  if( i == int(sys.argv[1]) ):
    return 
  sum = x+y
  fibolist.append(sum)
  fibonacci(y, sum)
   
fibonacci(1,1)
print fibolist[-1]

