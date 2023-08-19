import sys
sys.stdin = open("3_input.txt", "r")


def DFS(v):
    if v == n+1:
        for c in range(1, n+1):
            if ch[c] == 1:
                print(c, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)
