t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a=sorted(l)
    if l==a:
        print("0")
    else:
        c=a[len(a)-1]-a[0]
        print(c)