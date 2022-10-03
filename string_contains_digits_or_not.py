for i in range(int(input())):
    l=input()
    for i in l:
        if i.isnumeric():
            print("Yes")
            break
    else:
        print("No")