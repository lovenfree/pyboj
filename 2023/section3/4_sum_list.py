import sys
sys.stdin = open("4_input.txt", "rt")

n = int(input())
a1 = input().split()
m = int(input())
a2 = input().split()

r = a1+a2
r.sort()

for x in (r):
    print(x, end=' ')
