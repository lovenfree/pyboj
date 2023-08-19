import sys
sys.stdin = open("4_input.txt", "rt")

n, c = map(int, input().split())

a = list()

for _ in range(n):
    a.append(int(input()))

a.sort()


def count(mid):
    x = 0
    r = 1
    for i in range(1, n):
        if a[i]-a[x] >= mid:
            r += 1
            x = i
    return r


lt = a[0]
rt = a[n-1]
result = 0

while lt < rt:
    mid = (lt+rt)//2
    if count(mid) >= c:
        result = mid
        lt = mid+1
    else:
        rt = mid-1


print(result)
