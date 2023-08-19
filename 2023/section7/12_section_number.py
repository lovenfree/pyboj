import sys
sys.stdin = open("12_input.txt")

dx=[-1,0,1,0]
dy=[0,1,0,-1]


def dfs(x,y):
    global cnt
    cnt+=1
    board[x][y] = 0

    for i in range(4):
        nx = x+dx[i] 
        ny = y+dy[i]

        if 0<=nx<size and 0<=ny<size and board[nx][ny]==1:
            board[nx][ny]=0
            cnt+=1
            dfs(nx,ny)

if __name__=="__main__":
    size = int(input())
    ch = [[0]*size for _ in range(size)]

    board = [list(map(int, input())) for _ in range(size)]
    print(board)
    res = list()

    for i in range(size):
        for j in range(size):
            if board[i][j]==1:
                cnt=0
                dfs(i,j)
                res.append(cnt)
    print(len(res))