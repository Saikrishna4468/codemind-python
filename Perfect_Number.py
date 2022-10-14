n=int(input())
mid=n//2
emt_lis=[i for i in range(1,mid+1) if n%i==0]
if sum(emt_lis)==n:
    print("True")
else:
    print("False")