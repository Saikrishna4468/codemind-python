l=input()
for i in range(len(l)):
    if l.count(l[i])==1:
        print(i)
        break
else:
    print("-1")