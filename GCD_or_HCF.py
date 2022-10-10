a,b=map(int,input().split())
a1=[]
b1=[]
op=[]
for i in range(1,a+1):
    if a%i==0:
        a1.append(i)
for j in range(1,b+1):
    if b%j==0:
        b1.append(j)
for i in a1:
    if i in b1:
        op.append(i)
print(max(op))