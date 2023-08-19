import sys
sys.stdin = open("input_9.txt", "rt")

n = int(input())
a = list()

for i in range(n):
    a.append(list(map(int, input().split())))

max = 0

for i in a:
    d = [1]*7
    for j in i:
        d[j] += 1

    m = 0
    for i in range(1, 7):
        if d[i] == 3:
            m = 10000+i*1000
            break
        elif d[i] == 2:
            m = 1000+i*100
            break
        else:
            m = i*100
    if max < m:
        max = m

print(max)
