a,b=map(int,input().split())
a1=[]
b1=[]
op=[]
for i in range(1,50+1):
        a1.append(a*i)
for j in range(1,50+1):
        b1.append(b*j)
for i in a1:
    if i in b1:
        op.append(i)
        break
print(*op)