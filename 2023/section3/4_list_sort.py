import sys
sys.stdin = open("4_input.txt", "rt")

n = int(input())
a1 = list(map(int, input().split()))
m = int(input())
a2 = list(map(int, input().split()))

r = list()
p1 = p2 = 0
c = True
while p1 < n and p2 < m:
    if a1[p1] < a2[p2]:
        r.append(a1[p1])
        p1 += 1
    else:
        r.append(a2[p2])
        p2 += 1

if p1 < n:
    r = r+a1[p1:n]
if p2 < m:
    r = r+a2[p2:m]
print(r)
