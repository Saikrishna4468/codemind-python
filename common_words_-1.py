s1=input().lower().split()
s2=input().lower().split()
c=0
for i in s1:
    if i in s2:
        c+=1
print(c)