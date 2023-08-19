import sys
sys.stdin = open("input.txt", "r")


def dfs(L, sum):

    if L == n:
        if sum == f:
            for j in res:
                print(j, end=' ')
        print()
        return

    else:

        fo


if __name__ == "__main__":
    n, f = map(int, input().split())

    b = []
    b[0] = 1
    for i in range(1, n-1):
        b[i] = n-1

    b[n] = 1
    res = [0]*n
    ch = [0]*(n+1)

    dfs(0)
