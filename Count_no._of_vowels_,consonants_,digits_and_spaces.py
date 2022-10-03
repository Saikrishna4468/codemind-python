l=input()
Vowel=0
Consonants=0
Digits=0
Whitespace=0
vo="aeiouAEIOU"
for i in l:
    if i.isalpha():
        if i in vo:
            Vowel+=1
        else:
            Consonants+=1
    else:
        if i.isnumeric():
            Digits+=1
        else:
            Whitespace+=1
print("Vowels:",Vowel)
print("Consonants:",Consonants)
print("Digits:",Digits)
print("White spaces:",Whitespace)