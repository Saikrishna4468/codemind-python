def ele_maj(n,l):
    d={}
    for i in range(0,n):
        if l[i] in d.keys():
            d[l[i]]+=1
        else:
            d[l[i]]=1
    k=max(d.values())
    for i,j in d.items():
        if j==k:
            return i
n=int(input())
l=list(map(int,input().split()))
print(ele_maj(n,l))