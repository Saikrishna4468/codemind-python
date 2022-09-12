n,k=map(int,input().split())
a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if sum(a[i:j])==k:
            count+=1
print(count)