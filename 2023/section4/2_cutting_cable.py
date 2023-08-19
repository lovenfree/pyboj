import sys
sys.stdin = open("2_input.txt", "rt")

k, n = map(int, input().split())
a = list()

l = 0

for i in range(k):
    tmp = int(input())
    a.append(tmp)
    l = max(l, tmp)


lt = 1
rt = l

result = 0
while lt <= rt:
    sum = 0

    mid = (lt+rt)//2

    for i in a:
        sum += i//mid

    if sum >= n:
        result = mid
        lt = mid+1
        break
    elif sum < n:
        rt = mid-1
