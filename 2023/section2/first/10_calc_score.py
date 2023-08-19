import sys
sys.stdin = open("input_10.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

c = 0
s = 0
for i in a:
    if i == 1:
        c += 1
        s += c
    elif i == 0:
        c = 0

print(s)
