import sys
from collections import deque

sys.stdin = open("input.txt","r")

n = int(input())



# 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

a=[list(map(int, input().split)) for _ in range(n)]
ch = [[0]*n for _in range(n)]

sum=0

Q= deque()
ch[n//2][n//2]=1
sum+=a[n//2][n//2]
Q.append((n//2,n//2))

while True:
    now = Q.popleft()
    for i in range (len(a)):

        nx = now[0]+dx[i]
        ny = now[1]+dy[i]

        if nx>0 and ny <= n:
            if ch[nx][ny]!=1:
                sum+=a[nx][ny]
                ch[nx][ny] = 1
                Q.append((nx,ny))
