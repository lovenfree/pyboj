import sys
sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
reulst = list(res)
reulst.sort(reverse=True)
# print(reulst[k])
print(reulst[k-1])
