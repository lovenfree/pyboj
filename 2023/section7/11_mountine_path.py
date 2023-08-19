import sys
sys.stdin = open("11_input.txt","rt")


dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):

    global cnt

    if x==ex and y==ey:
        cnt+=1
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<size and 0<=ny<size and ch[nx][ny]==0:
            if board[nx][ny]> board[x][y]:
                ch[nx][ny]=1
                dfs(nx,ny)
                ch[nx][ny]=0

if __name__=="__main__":

    min=219000000
    max=-2190000000
    size = int(input())
    # sx,sy,ex,ey=0
    board=[[0]*size for _ in range(size)]
    ch=[[0]*size for _ in range(size)]
   
    for i in range(size):
        a = list(map(int,input().split()))
        for j in range(size):
            if a[j]<min:
                min = a[j]
                sx=i
                sy=j
            elif a[j]>max:
                max = a[j]
                ex = i
                ey = j
            board[i][j]=a[j]

    ch[sx][sy]=1
    cnt=0
    dfs(sx,sy)
    print(cnt)