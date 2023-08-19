import sys
sys.stdin = open("5_input.txt", "rt")


def dfs(A, S):
    global result

    if S > c:
        return

    if A == n:
        if result < S:
            result = S
    else:
        dfs(A+1, S+a[A])
        dfs(A+1, S)


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = []

    for i in range(n):
        a.append(int(input()))
    print(c, n)
    print(a)

    result = 0
    dfs(0, 0)
    print(result)
