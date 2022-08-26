def ugly(n):
    k=n
    while k%2==0:
        k=k//2
    while k%3==0:
        k=k//3
    while k%5==0:
        k=k//5
    if k==1:
        return "Ugly Number"
    else:
        return "Not Ugly Number"
print(ugly(int(input())))