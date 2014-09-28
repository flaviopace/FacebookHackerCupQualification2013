import sys
import math
from collections import Counter
 
in_file = open(sys.argv[1],&quot;r&quot;)
exp = in_file.read()
in_file.close()
 
a= exp.split(&quot;\n&quot;)
 
b=[]
c=[]
 
values=[]
 
d={}
u={}
 
for i in range(1, len(a)-1) :
 
    b.append(a[i].lower()[::-1])
 
flavio=1
for i in b:
    d={}
 
    values=[]
    num=26
    find=1
    numSum=0
    for k in range(0,len(i)):
 
        #d[str(i[k])] = i.count(i[k])
        if(str(i[k]).isalpha()):# or str(i[k])=='!'):
            d[str(i[k])] = i.count(i[k])
 
    for k in range(0,len(i)):
        if (str(i[k]) in d):
        #   print i[k] + &quot; num &quot;+ str(num) + &quot; # &quot; + str(d[i[k]])
            numSum += num*d[i[k]]
            values.append(d[i[k]])
            del d[i[k]]
            num -=1
 
    values_sorted= sorted(values, reverse=True)
 
    num=26
    numSum =0
    for item in range(len(values_sorted)):
 
        numSum += num * values_sorted[item]
        num -=1
    print &quot;Case #&quot; + str(flavio)+ &quot;: &quot; +str(numSum)
    flavio +=1
