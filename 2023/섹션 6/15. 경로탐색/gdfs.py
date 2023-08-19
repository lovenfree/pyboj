import sys
sys.stdin = open("input.txt", "r")

def dfs(L):
    global count
    if L==node:
        count+=1
    else:
        for i in range (1, node+1):
            if dup[i]==0 and g[L][i]==1 :
                dup[i] = 1
                dfs(i)
                dup[i] = 0






if __name__=="__main__":
    node, path = map(int, input().split())


    g=[[0]*(node+1) for _ in range (node+1)]
    dup = [0]*(node+1)

    for i in range(path):
        a,b = map(int,input().split())
        g[a][b] =1

    # for i in range(1, node+1):
    #     for j in range (1, node+1):
    #         print(g[i][j], end =' ')
    #     print()

    count = 0
    dup[1] = 1
    dfs(1)
    print(count)
