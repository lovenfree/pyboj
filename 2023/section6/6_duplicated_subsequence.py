import sys
sys.stdin = open("6_input.txt", "rt")


def dfs(L):
    global cnt
    if L == m:
        for j in range(0, m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[L] = i
            dfs(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    # print(n, m)
    cnt = 0
    res = [0]*m
    dfs(0)
    print(cnt)
