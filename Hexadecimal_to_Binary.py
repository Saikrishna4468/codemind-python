a=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
b=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
for _ in range(int(input())):
    n=input()
    c=''
    for i in n:
        if i in a:
            f=a.index(i)
            c+=b[f]
    print(c)