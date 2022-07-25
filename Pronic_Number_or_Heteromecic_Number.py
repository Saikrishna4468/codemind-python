def pro(a):
    for i in range(1,a+1):
        for j in range(1,a+1):
            if (a%i==0) and (a%j==0) and (i-j==1 or j-i==1):
                if i*j==a:
                    return a
                break
x=int(input())
if pro(x)==x:
    print("YES")
else:
    print("NO")