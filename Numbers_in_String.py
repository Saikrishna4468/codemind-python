l=input()
c=0
for i in l:
    if i.isnumeric():
        c+=int(i)
print(c)