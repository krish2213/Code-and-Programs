s=input().strip()
ind_vowel=len(s)-1
for i in s[::-1]:
    if i.lower() in "aeiou" :
        vowel=i
        print("Index of first vowel from the last in the given string is",ind_vowel)
        break
    ind_vowel+=1
ind_consonant=0
for j in s:
    
    if j.lower() not in "aeiou":
        consonant=j
        print("Index of first consonant from the first is ",ind_consonant)
        break
    ind_consonant+=1
for k in range(len(s)):
    if k == ind_vowel:
        print(consonant,end="")
    elif(k==ind_consonant):
        print(vowel,end="")
    else:
        print(s[k],end="")
