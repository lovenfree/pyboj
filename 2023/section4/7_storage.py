import sys
sys.stdin = open("7_input.txt", "rt")

w = int(input())
a = list(map(int, input().split()))
m = int(input())
while 0 < m-1:
    l = min(a)
    h = max(a)
    lid = 0
    hid = 0

    for x in range(0, w):
        if a[x] == l:
            lid = x
            break

    for x in range(0, w):
        if a[x] == h:
            hid = x
            break
    a[lid] += 1
    a[hid] -= 1
    m -= 1

print(max(a)-min(a))
