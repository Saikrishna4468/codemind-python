s=input().split()
c=[]
if len(s)>1:
    for i in s:
        c.append(s[-1])
        break
    c="".join(c)
    for i in c:
        print(i)
        break
else:
    b=" ".join(s)
    for i in b:
        print(i)
        break