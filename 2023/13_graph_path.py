import sys
sys.stdin = open("13_input.txt", "rt")


def dfs(N):
    global cnt
    if N==n:
        cnt+=1
    else:

        for i in range(1, n+1):
            if g[N][i]==1 and ch[i] ==0 #N에서 i로 갈수 있냐 & 한번도 안갔냐
            ch[i]=1


if __name__ == "__main__":

    n, m = map(int, input().split())
    g = [[0]*(n+1) for _ in range(n+1)]

    ch = [0]*(n+1)
    for i in range(m):
        x, y = map(int, input().split())
        g[x][y] = 1
    cnt=0
    ch[1] = 1
    dfs(1)
