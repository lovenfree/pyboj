import sys
from collections import deque
sys.stdin = open("5_input.txt", "rt")

n, k = map(int, input().split())
q = deque()
cnt = 0

for i in range(1, 9):
    q.append(i)

while len(q) > 1:
    temp = q.popleft()
    cnt += 1
    if cnt % 3 != 0:
        q.append(temp)


print(q)
