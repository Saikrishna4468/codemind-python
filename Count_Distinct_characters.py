s=input()
s=s.lower()
c=[]
for _ in s:
    if _ not in c:
        c.append(_)
a=("".join(c).replace(" ",""))
print(len(a))