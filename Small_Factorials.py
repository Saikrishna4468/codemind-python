def factorial(n):
     return 1 if (n==1 or n==0) else n*factorial(n-1)
for i in range(int(input())):
    n=int(input())
    print(factorial(n))