n=int(input())
l=list(map(int,input().split()))
el=[]
c=0
for i in l:
    for j in l:
        if i>j:
            c+=1
    el.append(c)
    c=0
print(*el)