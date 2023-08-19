import sys
sys.stdin = open("13_input.txt","rt")
from collections import deque


size = int(input())
Q=deque()
board = [list(map(int,input().split())) for _ in range(size)]
res = list()

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
cnt=0
for i in range(size):
    for j in range(size):
        
        if board[i][j] ==1 :
            Q.append((i,j))
            board[i][j]=0
            cnt+=1

            while Q:
                t = Q.popleft()
                for x in range(8):
                    nx=dx[x]+t[0]
                    ny=dy[x]+t[1]

                    if 0<=nx<size and 0<=ny<size and board[nx][ny]==1 :
                        
                        board[nx][ny]=0
                        cnt+=1
                        Q.append((nx,ny)) 
            res.append(cnt)
            cnt=0


print(len(res))