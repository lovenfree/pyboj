import sys
sys.stdin = open("11_input.txt", "rt")


def dfs(L, start, sum):

    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
        return

    else:
        for x in range(start, n):
            dfs(L+1, x+1, sum+a[x])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    dfs(0, 0, 0)
    print(cnt)
