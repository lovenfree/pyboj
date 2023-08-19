import sys
sys.stdin = open("6_input.txt", "rt")

n = int(input())
a = []

for _ in range(0, n):
    h, w = map(int, input().split())
    a.append((h, w))

a.sort(reverse=True)

cnt = 0

# for i in range(1, n):
#     tmp = a[i]
#     for x in range(i-1, 0, -1):
#         if tmp[1] < a[x][1]:
#             break
#         elif tmp[1] > a[x][1] & i == 0:
#             cnt += 1

# print(cnt)

# 몸무게의 최대 최소
largest = 0
for p in a:
    if p[1] > largest:
        largest = p[1]
        cnt += 1

print(cnt)
