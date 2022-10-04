n=int(input())
l=list(map(int,input().split()))
n1=int(input())
if n1>n:
    n1=n1%n
z=l[-n1:]+l[:-n1]
print(*z)