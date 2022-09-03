n=int(input())
fc=0
for i in range(2,n):
    if n%i==0:
        fc+=1
if fc==0:
    print("prime")
else:
    print("not a prime")