import sys
def input(): return sys.stdin.readline().rstrip()


s = list(input())
result = [-1]*26


for i in range(len(s)):
    idx = ord(s[i])-97
    if result[idx] == -1:
        result[idx] = i

for i in range(26):
    print(result[i], end=' ')
