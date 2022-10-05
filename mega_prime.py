n=input()
l=list(n)
def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
list1=[int(i) for i in l]
opt=[prime(i) for i in list1]
print("Mega Prime" if prime(int(n)) and all(opt) else "Not Mega Prime")