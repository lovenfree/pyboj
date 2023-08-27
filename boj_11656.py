import sys
def input(): return sys.stdin.readline().strip()


s = input()
result = list()

for i in range(len(s)):
    result.append(str(s[i:]))

result.sort()

print('\n'.join(result))
