import sys
sys.stdin = open("9_index.txt","rt")
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

a=[list(map(int, input().split( ))) for _ in range(7)]


for i in range(7):
    for j in range(7):
        print(a[i][j], end=' ')
    print()
#이동경로 카운트    
ch = [[0]*7 for _ in range(7)]
dQ = deque()
print()
dQ.append((0,0))
a[0][0] =1

while dQ:
    c = dQ.popleft()

    for i in range(4):
        nx = c[0]+dx[i]
        ny = c[1]+dy[i]
        if 0<=nx <7 and 0<=ny<7:
   
            if a[nx][ny]==0:
                a[nx][ny]=1
                ch[nx][ny]=ch[c[0]][c[1]]+1
                # print(nx,ny,ch[nx][ny])
                dQ.append((nx,ny))


for i in range(7):
    for j in range(7):
        print(ch[i][j], end=' ')
    print()
     
if ch[6][6]==0:
    print(-1)
else:
    print(ch[6][6])
        
        
