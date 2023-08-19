import sys
sys.stdin = open("5_input.txt", "rt")

n = int(input())
a = []

for i in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

a.sort(key=lambda x: (x[1], x[0]))
# print(a)
cnt = 1
end = a[0][1]
# print(end[1])

for x in range(1, n):
    tmp = a[x]
    if tmp[0] >= end:
        cnt += 1
        end = tmp[1]


print(cnt)
