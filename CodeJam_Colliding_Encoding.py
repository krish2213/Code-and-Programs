'''Problem
Alan just had his first cryptography class in school today. He decided to apply what he learned and come up with his own cipher.
He will map each English letter from A to Z to a decimal digit 0 through 9
He will then try to encode each word to a string consisting of decimal digits by replacing each letter in the word with its mapped digit.
In his excitement, Alan failed to notice that there are 26 letters in the English alphabet and only 10
decimal digits. As a result, there might be collisions, that is, pairs of different words whose encoding is the same.
Given a list of N words that Alan wants to encode and the mapping that he uses, can you find out if there would be any collisions between words on the list?
Input
The first line of the input gives the number of test cases, T. T test cases follow.
The first line of each test case contains 26 decimal digits (integers between 0 and 9, inclusive) DA,DB,…,DZ, representing the mapping that Alan uses. 
A letter α is mapped to digit Dα. The second line of each test case contains N, the number of words Alan will encode.
The i-th of the last N lines contains a string Si, representing the i-th word Alan will encode.
Output
For each test case, output one line containing Case #x: y, where xis the test case number (starting from 1) and y
 is either YES, if there is at least one pair of different words from the list whose encoding coincides, and NO otherwise.
'''
testcase= int(input())
for i in range(testcase):
    final = []
    lis = list(map(int, input().split()))
    mydict = {chr(65+z): lis[z] for z in range(26)}
    n = int(input())
    strlist = []
    for j in range(n):
        mystr = input().strip()
        num = ''.join(str(mydict[l]) for l in mystr)
        final.append(num)
    if len(final) == len(set(final)):
        print("Case #"+str((i+1))+": NO")
    else:
        print("Case #"+str((i+1))+": YES")
