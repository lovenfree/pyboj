import sys
sys.stdin = open("8_input.txt", "r")

n = int(input())
p = dict()

for i in range(n):
    w = input()
    p[w] = 1

print(p)
for i in range(n-1):
    w = input()
    p[w] = 0

print(p)
for key, value in p.items():
    if value == 1:
        print(key)
