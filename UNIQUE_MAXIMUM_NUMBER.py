n=int(input())
l=list(map(int,input().split()))
g=[i for i in l if l.count(i)==1]
if len(g)==0:
    print("-1")
else:
    print(max(g))