l=input()
c=0
for i in l:
    if i.isnumeric():
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains",c,"digit")