import sys


def dfs(L, sum):
    global min

    if L >min:
        return
    if sum > total:
        return
    if sum == total:
        if L < min:
            min = L
        return

    for i in range(0, kind):

        dfs(L + 1, sum + money[i])


if __name__ == "__main__":
    kind = 3
    money = [1, 2, 5]
    total = 15
    min = 99999999
    money.reverse()
    dfs(0,0)
    print(min)
