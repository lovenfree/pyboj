import sys
sys.stdin = open("9_anagram.txt", "r")

str1 = dict()
str2 = dict()


s1 = input()
s2 = input()

for x in s1:
    str1[x] = str1.get(x, 0)+1

for x in s2:
    str2[x] = str2.get(x, 0)+1

if str1 == str2:
    print("YES")
else:
    print("NO")
