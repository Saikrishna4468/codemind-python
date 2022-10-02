n=int(input())
l=list(map(int,input().split()))
empty_list=[]
for i in l:
    empty_list.append(i*i)
print(*sorted(empty_list))