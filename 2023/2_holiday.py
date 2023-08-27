import sys
sys.stdin = open("2_input.txt", "rt")


def dfs(L, sum):
    global max
    if L == n:
        if max < sum:
            max = sum
    else:
        if L+times[L] < n:
            dfs(L+times[L], sum+points[L])
        dfs(L+1, sum)


if __name__ == "__main__":
    n = int(input())

    times = list()
    points = list()
    max = 0
    for i in range(n):
        t, p = map(int, input().split())
        times.append(t)
        points.append(p)

    dfs(0, 0)
    print(max)
