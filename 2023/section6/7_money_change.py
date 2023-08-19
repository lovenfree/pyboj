import sys
sys.stdin = open("7_input.txt", "rt")


def dfs(L, changes):
    global min
    if L > min:
        return

    if changes > c:
        return

    if changes == c:
        if min > L:
            min = L
        return
    else:
        for i in m:
            # changes += i
            dfs(L+1, changes+i)


if __name__ == "__main__":
    n = int(input())
    m = list(map(int, input().split()))
    c = int(input())

    min = 2147000000
    m.sort(reverse=True)

    dfs(0, 0)
    print(min)
