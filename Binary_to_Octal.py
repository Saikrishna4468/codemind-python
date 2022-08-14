for _ in range(int(input())):
    a=reversed(input())
    b=c=0
    for i in a:
        if i=='1':
            b=b+2**c
        c+=1
    d=oct(b)
    print(d[2:])