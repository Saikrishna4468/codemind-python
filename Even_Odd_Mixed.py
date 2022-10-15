n=input()
#print(n)
ec=0
oc=0
l=len(n)
for i in n:
    if int(i)%2==0:
        ec+=1
    else:
        oc+=1
if ec==0 and oc==l:
    print("Odd")
elif ec==l and oc==0:
    print("Even")
else:
    print("Mixed")