a,b=map(str,input().split())
b=int(b)
a1="".join(a[:b])
a2="".join(a[-b:])
print(abs(int(a1)-int(a2)))