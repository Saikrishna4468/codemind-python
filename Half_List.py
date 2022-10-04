n=int(input())
l=list(map(int,input().split()))
a=l[::-1]
b=[]
for i in range(n//2):
    b.append(a[i])
b.extend(l[:n//2])
print(*b)