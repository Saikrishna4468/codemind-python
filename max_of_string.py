a="abcdefghijklmnopqrstuvwxyz"
n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
g=[]
l=input().lower().replace(" ","")
for i in l:
    k=a.index(i)
    g.append(k)
print(a[max(g)])