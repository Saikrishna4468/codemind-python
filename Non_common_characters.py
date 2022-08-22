s1=input().lower().replace(" ","")
s2=input().lower().replace(" ","")
s3=""
s4=""
s5=""
for i in s1:
    if i not in s3:
        s3+=i
for i in s2:
    if i not in s4:
        s4+=i
for i in s3:
    if i not in s4:
        s5+=i
for i in s4:
    if i not in s3:
        s5+=i
print(len(s5))