import sys
sys.stdin = open("1_input.txt", "r")


def dfs(n):
    if n == 0:
        return

    dfs(n//2)
    print(n % 2, end=' ')


if __name__ == "__main__":
    n = int(input())
    dfs(n)
