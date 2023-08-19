import sys
sys.stdin = open("9_input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    for j in range(n):
        v = a[i][j]
        # 상 하 좌 우
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        for t in range(4):
            nx = i+x[t]
            ny = j+y[t]

            if nx < 0 or nx > n-1:
                continue
            if ny < 0 or ny > n-1:
                continue

            print(nx, ny, n)

            if a[nx][ny] > v:
                break
        else:
            cnt += 1

print(cnt)
