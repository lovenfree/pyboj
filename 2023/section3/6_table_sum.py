import sys
sys.stdin = open("input_6.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

max = 0

# array = [[0 for col in range(11)] for row in range(10)]
# array = [[0]*11 for i in range(10)]
# array = [[0]*11 ]*10

# 행
for i in a:
    if max < sum(i):
        max = sum(i)

# 열
for i in range(n):

    if max < sum([x[i] for x in a]):
        max = sum([x[i] for x in a])

sum1 = sum2 = 0
# 대각선
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]

if max < sum1:
    max = sum1

if max < sum2:
    max = sum2

print(max)
