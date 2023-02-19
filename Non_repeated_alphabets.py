#Accept a list of strings and count the number of strings having atmost k non-repeated alphabets
n,k=map(int,input().split()) #n is the number of strings
count = 0 #count of strings 
for i in range(n):
    string = input().strip()
    temp=0
    for letter in string:
        if string.count(letter) == 1:
            temp+=1
    if temp<=k: #atmost k
        count+=1
print(count)
