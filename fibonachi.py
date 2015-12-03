#!/usr/bin/env python
import sys
import re
sys.setrecursionlimit(10000)

def usage():
  print "Usage: %s [seq_number]\n\tseq_number should be between 2 and 9998" % sys.argv[0]
  exit(1)

if( len(sys.argv) < 2 ):
  usage()
print sys.argv[1]
if( int(sys.argv[1]) < 2 or int(sys.argv[1]) > 9998 ):
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

