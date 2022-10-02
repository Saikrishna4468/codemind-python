n=int(input())
l=list(map(int,input().split()))
k=abs((sum(l[:len(l)//2]))-(sum(l[len(l)//2:])))
if k%4==0:
    print("X")
else:
    print("Y")