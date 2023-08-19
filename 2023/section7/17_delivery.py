import sys
sys.stdin=open("17_input.txt","rt")

def DFS(L,S):
    global res 
    if L==m:
        sum=0
        for hi in range(len(h)):
            hx = h[hi][0]
            hy = h[hi][1]

            dis = 2147000000
            
            for x in cb:
                x2 = p[x][0]
                y2 = p[x][0]

                dis = min(dis, abs(hx-x2)+abs(hy-y2))
            sum+=dis 
        if sum<res:
            res = sum
            # print(x,end=' ')
        # print()
    else:
        for i in range(S,len(p)):
            cb[L]=i
            DFS(L+1,i+1)

    
if __name__=="__main__":
    res = 217000000
    n,m=map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(n)]

    p=[]
    h=[]
    cb=[0]*m #조합의 경우의 수
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1: 
                h.append((i,j))
            elif board[i][j] ==2:
                p.append((i,j))
    DFS(0,0)
    print(res)
        