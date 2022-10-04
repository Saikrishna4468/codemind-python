n=int(input())
m=int(input())
c=0
k=[k for k in range(n,m+1)]
for i in range(len(k)):
    for j in range(i+1,len(k)+1):
        if sum(k[i:j])%2!=0:
            c+=1
print(c)