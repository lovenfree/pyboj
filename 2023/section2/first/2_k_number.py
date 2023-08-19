import sys
sys.stdin = open("input.txt", "rt")

c = int(input())

for i in range(c):
    N, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))
    sort = a[s-1:e]
    sort.sort()
    # print(sort[k])
    print("#%d %d" % (i+1, sort[k-1]))
