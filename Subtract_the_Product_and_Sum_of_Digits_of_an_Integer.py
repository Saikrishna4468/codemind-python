n=(input())
pro=1
summ=0
for i in n:
    pro*=int(i)
    summ+=int(i)
print(pro-summ)