import sys
sys.stdin = open("7_input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

s = e = n//2
sum = 0


for i in range(n):
    # print(s, e+1)
    for x in range(s, e+1):
        # print(a[i][x], end=' ')
        sum += a[i][x]

    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1


print(sum)
