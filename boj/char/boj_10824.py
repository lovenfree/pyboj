import sys
def input(): return sys.stdin.readline().strip()


s = list(input().split(' '))

print(int(s[0]+s[1])+int(s[2]+s[3]))
