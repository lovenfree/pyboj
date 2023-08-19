import sys
sys.stdin = open("16_input.txt","rt")

board = [list(map(int,input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]

dx=[0,-1,0]
dy=[-1,0,1]

def DFS(x,y):
    ch[x][y]=1

    if x==0:
        print(y)
        return
    else:
        #왼
        if 0<=y-1<10 and board[x][y-1]==1 and ch[x][y-1]==0:
            DFS(x, y-1)
        #오
        elif 0<=y+1<10 and  board[x][y+1]==1 and ch[x][y+1]==0:
            DFS(x, y+1)
        #위
        # elif 0<=x-1<10 and ch[x-1][y]==0:
        else:
            DFS(x-1, y)
        
if __name__=="__main__":
    for i in range(10):
        if board[9][i]==2:
            DFS(9,i)
