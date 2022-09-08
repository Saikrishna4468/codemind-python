l=input().lower().split()
count=0
for i in l:
    if i==str(i[::-1]):
        count+=1
print(count)