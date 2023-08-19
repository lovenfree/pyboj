import sys
sys.stdin = open("15_input.txt","rt")
from collections import deque

Q = deque()

dx=[-1,0,1,0]
dy=[0,1,0,-1]

m,n = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
dis = [[0]*m for _ in range(n)]
Q=deque()

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            Q.append((i,j))
            dis[i][j]=0
            board[i][j]=1

while Q:
    t = Q.popleft()

    for i in range(4):
        nx=dx[i]+t[0]
        ny=dy[i]+t[1]

        if 0<=nx<n and 0<=ny<m and board[nx][ny]==0:
                Q.append((nx,ny))
                dis[nx][ny]=dis[t[0]][t[1]]+1
                board[nx][ny]=1    

b = 0
for i in range(n):
     for j in range(m):
          if dis[i][j] > b:
               b = dis[i][j]
print(b)