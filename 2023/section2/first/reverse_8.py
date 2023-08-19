import sys
sys.stdin = open("input_8.txt", "rt")


n = int(input())
a = list(map(int, input().split()))


def reverse(x):
    res = 0

    while x > 0:
        res = res*10 + (x % 10)
        x = x//10

    return res


for x in a:
    print(reverse(x), end=' ')
