s=input()
s=s.lower()
c=[]
for i in s:
    if i not in c:
        c.append(i)
print("".join(sorted(c)).replace(" ",""))