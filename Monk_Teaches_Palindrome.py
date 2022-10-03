for i in range(int(input())):
    l=input()
    l1="".join(l[::-1])
    if l==l1:
        if len(l)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
        