import sys
sys.stdin = open("8_input.txt", "rt")


def dfs(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                dfs(L+1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    # print(n, m)
    res = [0]*n
    ch = [0]*(n+1)  # 중복 허용 안함
    cnt = 0
    dfs(0)
    print(cnt)
