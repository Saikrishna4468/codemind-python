n=int(input())
#l=input()
l=input().replace(" ","").split("0")
print(max([len(i) for i in l]))