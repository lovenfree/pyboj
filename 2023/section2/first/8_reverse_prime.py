import sys
sys.stdin = open("input_8.txt", "rt")

n = int(input())
a = list(input().split())


def reverse(x):
    return int(x[::-1])


def is_Prime(x):
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True


# x[0]
# x[2:4] index 2,3
# x[:3] index 0,1,2
# x[1:] index 1 부터 끝까지
for x in a:
    r = reverse(x)
    if is_Prime(r):
        print(r, end=' ')
