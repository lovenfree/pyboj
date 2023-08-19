import sys
sys.stdin = open("input_6.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

max = -2147000000


def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum


for i in a:
    tot = digit_sum(i)

    if tot > max:
        max = tot
        res = i

print(res)
