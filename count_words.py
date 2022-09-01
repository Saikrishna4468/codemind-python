s=input().lower().split()
a="aeiou"
c=0
fl=[]
ll=[]
for i in s:
    d=str(i)
    fl.append(d[0])
    ll.append(d[-1])
j=0
for i in fl:
    if i in a and ll[j] not in a:
        c+=1
    j+=1
print(c)