sl="abcdefghijklmnopqrstuvwxyz"
sln=[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
cl="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cln=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
n=input()
if n.islower():
    c=sl.index(n)
    print(sln[c])
elif n.isupper():
    d=cl.index(n)
    print(cln[d])