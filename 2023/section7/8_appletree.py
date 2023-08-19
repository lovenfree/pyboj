import sys
sys.stdin = open("_input.txt","rt")
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]
n = int(input())
a=[list(map(int,input().split())) for _ in range(n)]

dq = deque()
s=n//2

res = 0
ch=[[0]*n for _ in range(n)]
# res+=a[s][s]
dq.append((s,s))
L=0
while True:
    if L==n//2:
        break
    size = len(dq)
    for i in range(size):
        tmp = dq.popleft()

        
        for j in range(4):
            nx = tmp[0]+dx[j]
            ny = tmp[1]+dy[j]
            if ch[nx][ny]==0:
                res+=a[nx][ny]
                dq.append((nx,ny))
                ch[nx][ny]=1
    L+=1


print(res)





