import sys
from collections import deque
sys.stdin = open("8_input.txt", "rt")

n, w = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
p = deque(a)
cnt = 0

while p:
    if len(p) == 1:
        cnt += 1
        break

    if p[0] + p[-1] <= w:
        p.pop()  # 맨뒷자리
        p.popleft()
        cnt += 1
    elif p[0] + p[-1] > w:
        p.pop()
        cnt += 1
        # print(a, rt)
print(cnt)
