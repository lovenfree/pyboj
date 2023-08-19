import sys
sys.stdin = open("10_input.txt", "rt")


def dfs(L, s):
    global cnt
    if L == m:
        for j in res:
            print(j, end=' ')
        cnt += 1
        print()
    else:
        for x in range(s, n+1):
            res[L] = x
            dfs(L+1, x+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    res = [0]*m
    dfs(0, 1)
    print(cnt)
