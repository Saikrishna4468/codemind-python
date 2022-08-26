n=int(input())
a,b=0,1
c=[0,1]
while True:
    d=a+b
    c.append(d)
    a,b=b,d
    if d>n:
        break
print(n in c)