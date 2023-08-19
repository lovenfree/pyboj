import sys
sys.stdin = open("8_input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
ra = [list(map(int, input().split())) for _ in range(m)]

for i in ra:
    an = i[0]
    direction = i[1]
    num = i[2]

    # left
    if direction == 0:
        for j in range(num):
            c = a[an-1].pop(0)
            a[an-1].append(c)
    # right
    else:
        for j in range(num):
            c = a[an-1].pop()
            a[an-1].insert(0, c)


sum = 0

si, ei = 0, n-1
for i in range(0, n):
    for j in range(si, ei+1):
        sum += a[i][j]

    if i < n//2:
        si += 1
        ei -= 1
    else:
        si -= 1
        ei += 1

print(sum)
