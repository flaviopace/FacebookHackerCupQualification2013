mport sys
import math
from collections import Counter
import re
 
in_file = open(sys.argv[1],"r")
exp = in_file.read()
in_file.close()
 
 
b=[]
c=[]
 
values=[]
 
d={}
u={}
 
for i in range(1, len(a)-1) :
     
    b.append(a[i].lower())
 
replacements = {":(",":)"}
 
for i in range(0,len(b)) :
    #b[i]=   b[i].replace(
     
    b[i]=  re.sub(r'\([^)]*\)', "", b[i])
 
    b[i]=   b[i].replace(':(','')
    b[i]=   b[i].replace(':)','')   
 
 
 
 
def isBalanced(strInput):
    """Validate if an input string is having balanced bracket pairs
    this includes bracket ordering. i.e a round bracket must be closed
    by a round bracket.  Emtpy strings are treated as balanced."""
    #if strInput:
        # list of all bracket kinds, in paired tuples
    brackets = [ ('(',')'), ('[',']'), ('{','}')]
        # define fake constants - python does not support the concept of constants
    kStart = 0
    kEnd = 1
        # internal stack used to push and pop brakets in the input string
    stack = []
 
    for char in strInput:
         for bracketPair in brackets:
             if char == bracketPair[kStart]:
                  stack.append(char)
             elif char == bracketPair[kEnd] and len(stack) > 0 and stack.pop() != bracketPair[kStart]:
                  return False
 
    if len(stack) == 0:
        return True
 
    #return False
 
 
flavio=1
for i in range(0,len(b)) :
    if(isBalanced(b[i])):
        print "Case #" + str(flavio) + ": YES"
    else:
        print "Case #" + str(flavio) + ": NO"
 
    flavio +=1
