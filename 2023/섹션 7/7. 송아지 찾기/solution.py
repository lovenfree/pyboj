import sys
from collections import deque

sys.stdin = open("input.txt","r")

max = 10000

ch = [0]*(max+1)

n,m = map(int, input().split())
ch[n] = 1

q = deque()
q.append(n)

while q:
    now = q.popleft()
    for next in (now-1,now+1,now+5):
        if next>0 and next <=max:
            if ch[next]==0:
                if next == m:
                    print(ch[now]+1)
                    break
                else:
                    q.append(next)
                    ch[next] = ch[now]+1


