import sys
sys.stdin = open("input_6.txt", "rt")

n = int(input())
a = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


max = -2147000000

for i in a:
    tot = digit_sum(i)

    if tot > max:
        max = tot
        res = i

print(res)
