n=int(input())
a=0
b=1
g=[0,1]
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    g.append(c)
print(*g)