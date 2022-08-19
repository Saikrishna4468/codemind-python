s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
s3=" "
c=0
for i in s1:
    if i not in s3:
        s3+=i
for i in s3:
    if i in s2:
        c+=1
print(c)