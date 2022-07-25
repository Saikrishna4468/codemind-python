x=int(input())
s=x*x
a=str(s)
b=str(x)
if a.endswith(b):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")