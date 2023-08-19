import sys

sys.stdin = open("input.txt", "r")


def dfs(day, sum):
    global max

    if day == days:
        if sum > max:
            max = sum
    else:
        if day+spends[day]<=days:
            dfs(day+spends[day], sum + moneys[day])
        else:
            dfs(day + 1, sum)


if __name__ == "__main__":
    days = int(input())
    spends = list()
    moneys = list()
    max = 0

    for i in range(days):
        a, b = map(int, input().split())
        spends.append(a)
        moneys.append(b)

    dfs(0, 0)
    print(max)
