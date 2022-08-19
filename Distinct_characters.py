s=input()
s=s.lower().replace(" ","")
s=sorted(s)
for i in s:
    if s.count(i)==1:
        print(i,end="")