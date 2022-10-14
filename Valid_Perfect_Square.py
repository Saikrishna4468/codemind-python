for _ in range(int(input())):
    n=int(input())
    mid=n//2
    for i in range(1,mid+1):
        if i*i==n:
            print("True")
            break
    else:
        print("False")