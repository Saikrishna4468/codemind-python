n=int(input())
b=bin(n)
o=b[2:]
s=''
for i in o:
    if i=='1':
        s+='0'
    elif i=='0':
        s+='1'
x=s[::-1]
p=q=0
for i in x:
    if i=="1":
        p+=2**q
    q+=1
print(p)