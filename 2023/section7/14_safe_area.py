import sys
sys.stdin = open("14_input.txt","rt")
sys.setrecursionlimit(10**6)
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]


def dfs(x,y,h):
    global cnt
    ch[x][y]=1

    for j in range(4):
        nx=dx[j]+x
        ny=dy[j]+y

        if 0<= nx <size and 0<=ny<size and ch[nx][ny]==0 and board[nx][ny]>h:
            dfs(nx,ny,h)
            

if __name__=="__main__":

    size = int(input())
    board = [list(map(int,input().split())) for _ in range(size)]

    res=0

    for i in range(100):
        ch=[[0]*size for _ in range(size)]
        cnt=0
        for x in range(size):
            for y in range(size):
                if ch[x][y]==0 and board[x][y] > i:
                    cnt+=1
                    dfs(x,y,i)
        res=max(res,cnt)
        if cnt==0:
            break


    print(res)



