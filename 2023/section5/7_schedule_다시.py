import sys
from collections import deque
sys.stdin = open("7_input.txt", "r")


m = input()
n = int(input())
# q = deque(m)


for i in range(n):
    s = input()
    q = deque(m)

    for x in s:
        if x in q:
            if q.popleft() != x:
                print(i+1, " #No")
                break

    else:
        if len(q) > 0:
            print(i+1, " #No")

        elif len(q) == 0:
            print(i+1, " #YES")
