n=int(input())
l=list(map(int,input().split()))
l1=set(l)
c=0
for i in l1:
    k=l.count(i)
    c+=k//2
print(c)