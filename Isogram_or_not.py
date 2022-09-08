string=list(input().lower())
g=[]
for i in string:
    if string.count(i)==1:
        g.append(i)
if "".join(string)=="".join(g):
    print("True")
else:
    print("False")