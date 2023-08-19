def dfs(L, start, sum):
    global count
    if L == K:

        print(ch)
        if sum % M == 0:
            count += 1
        return
    else:

        for i in range(start, len(array)):
            ch[L] = array[i]
            dfs(L + 1, i + 1, sum + array[i])


if __name__ == "__main__":
    N = 5
    K = 3
    array = [2, 4, 5, 8, 12]
    M = 6
    count = 0
    ch = [0] * K
    dfs(0, 0, 0)
    print(count)
