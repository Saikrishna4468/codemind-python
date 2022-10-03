l=input()
st=input()
c=0
for i in l:
    if i==st:
        c+=1
if c==0:
    print("-1")
else:
    print(c)