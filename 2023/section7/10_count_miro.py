import sys
sys.stdin = open("10.input.txt","rt")

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x,y):
    global res

    if x==6 and y==6:
        res+=1
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<7 and 0<=ny<7 and a[nx][ny] == 0:
                a[nx][ny] =1
                dfs(nx,ny)
                a[nx][ny] =0

if __name__=="__main__":


    a=[list(map(int, input().split( ))) for _ in range(7)]
    # ch=[[0]*7 for _ in range(7)]

    res =0 
    a[0][0]=1
    dfs(0,0)
    print(res)