n=int(input())
l=list(map(int,input().split()))
m=max(l)
ex=int(input())
el=[]
for i in range(len(l)):
    if l[i]+ex>=m:
        el.append("True")
    else:
        el.append("False")
print(*el)