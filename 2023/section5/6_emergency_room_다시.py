import sys
from collections import deque
sys.stdin = open("6_input.txt", "rt")

n, m = map(int, input().split())
a = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
q = deque(a)

# target = q[m]
cnt = 0
print(max(q[1]))
while q:

    # e = max(q[1])
    i = q.popleft()
    if any(i[1] < x[1] for x in q):
        q.append(i)
    # print(i, e, q, cnt)
    else:
        cnt += 1


print(cnt)
