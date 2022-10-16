l=input().lower()
g=""
a="aeiou"
op=[]
for i in l:
    if i in a:
        g+="V"
    else:
        g+="C"
l=list(g)
op.append(g[0])
for i in l:
    if op[-1]!=i:
        op.append(i)
print("".join(op))