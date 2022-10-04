n=int(input())
x,s=[],0
for i in range(n):
    x.append(int(input()))
y=int(input())
for j in x:
    if j<=y:
        s+=1
    else:
        s+=2
print(s)