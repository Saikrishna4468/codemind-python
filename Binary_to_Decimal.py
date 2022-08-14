for _ in range(int(input())):
    a=reversed(input())
    c=d=0
    for i in a:
        if i=="1":
            c=c+2**d
        d+=1
    print(c)