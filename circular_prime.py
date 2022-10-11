def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
n=(input())
n1=n[::-1]
if prime(int(n)) and prime(int(n1)):
    print("circular prime")
elif prime(int(n))==False:
    print("not prime")
elif prime(int(n)) and (prime(int(n1))==False):
    print("prime but not a circular prime")
            