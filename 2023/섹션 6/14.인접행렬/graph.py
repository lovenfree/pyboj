import sys
sys.stdin=open("input.txt","r")
node, path = map(int, input().split())

g=[[0]*(node+1) for _ in range(node+1)]

for i in range(path):
    a, b =map(int, input().split)
    g[a][b] =1
    g[b][a] =1

for i in range(1, node+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()