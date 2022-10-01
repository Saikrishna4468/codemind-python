n=int(input())
l=list(map(int,input().split()))
g=[]
for i in l:
    if l.count(i)==1:
        g.append(i)
if len(g)==0:
    print("-1")
else:
    print(*g)