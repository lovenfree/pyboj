import sys
sys.stdin = open("12_input.txt")
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]


size = int(input())
board = [list(map(int, input())) for _ in range(size)]
res = list()
Q = deque()
cnt =0

for i in range(size):
    for j in range(size):
        if board[i][j]==1:
            Q.append((i,j))
            cnt+=1
            board[i][j]=0

            while Q:
                t = Q.popleft()
                for i in range(4):
                    nx = t[0]+dx[i] 
                    ny = t[1]+dy[i]

                    if 0<=nx<size and 0<=ny<size and board[nx][ny]==1:
                        Q.append((nx,ny))
                        board[nx][ny]=0
                        cnt+=1

            res.append(cnt)
            cnt=0

print(len(res))    