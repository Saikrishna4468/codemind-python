a=int(input())
b=int(input())
c=[]
d=[]
for i in range(1,a):
    if a%i==0:
        c.append(i)
for j in range(1,b):
    if b%j==0:
        d.append(j)
if sum(c)==b and sum(d)==a:
    print("Amicable")
else:
    print("Not Amicable")