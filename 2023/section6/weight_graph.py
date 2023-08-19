import sys
sys.stdin = open("11_input.txt", "rt")

n, m = map(int, input().split())

g = [[0]*(m+1) for _ in range(m+1)]

for i in range(m):
    x, y, w = map(int, input().split())
    g[x][y] = w

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()
