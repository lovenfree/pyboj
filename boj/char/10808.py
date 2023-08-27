import sys
def input(): return sys.stdin.readline().rstrip()


s = list(input())
result = [0]*26

for i in s:
    idx = ord(i)-97
    result[idx] = result[idx]+1

for i in range(26):
    print(result[i], end=' ')
