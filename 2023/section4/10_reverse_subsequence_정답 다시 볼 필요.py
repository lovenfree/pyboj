import sys
sys.stdin = open("10_input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
r = [0 for i in range(n)]


for i in range(1, n+1):
    idx = a[i-1]
    cnt = 0
    # print(idx, cnt, i)
    for b in range(len(r)):
        if r[b] != 0:
            continue
        if idx == cnt:
            r[b] = i
            break
        if r[b] == 0:
            cnt += 1
    print(r)
