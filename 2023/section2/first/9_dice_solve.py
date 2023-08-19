import sys
sys.stdin = open("input_9.txt", "rt")

n = int(input())

max = 0

for i in range(n):
    s = input().split()
    # string 일때 sort rksmd
    s.sort()
    a, b, c = map(int, s)

    if a == b & b == c:
        m = 10000+a*1000
    elif a == b | a == c:
        m = 1000+a*100
    elif b == c:
        m = 1000+b*100
    else:
        m = m = i*100

    if max < m:
        max = m

print(max)
