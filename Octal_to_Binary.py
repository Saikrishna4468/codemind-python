for _ in range(int(input())):
    n=input()
    c=[]
    d={"0":"000","1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
    for i in n:
        c.append(d[i])
    b="".join(c)   
    for i in range(len(b)):
        if b[i]=='1':
            print(b[i:])
            break
            
    #print(b.replace("0o",""))
