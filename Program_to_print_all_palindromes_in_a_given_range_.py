n1=int(input())
n2=int(input())
#print(n1,n2)
g=[]
for i in range(n1,n2+1):
    k=str(i)
    if k==k[::-1]:
        g.append(k)
print(*g)
    