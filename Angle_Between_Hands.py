a,b=map(int,input().split(":"))
c=[]
h1=a+(b/60)
h2=30*h1
m=6*b
d=abs(m-h2)
if d>180:
    d=360-d
print(d)