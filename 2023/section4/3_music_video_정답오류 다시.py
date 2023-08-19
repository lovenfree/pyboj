import sys
sys.stdin = open("3_input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

# print(n, m)
# print(sum(a))


def Count(capacity):
    cnt = 1
    sum = 0
    for i in a:
        if sum+i < capacity:
            sum += i
        elif sum+i >= capacity:
            cnt += 1
            sum = i
    return cnt


lt = 1
rt = sum(a)
result = 0

while lt < rt:
    mid = (lt+rt)//2

    if Count(mid) > m:
        lt = mid+1

    elif Count(mid) <= m:
        result = mid
        rt = mid-1

print(result)
