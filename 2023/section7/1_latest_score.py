import sys
sys.stdin = open("1_input.txt", "rt")


def dfs(L, sum, hour):
    global max
    if hour > m:
        return

    if L == n:
        if sum > max:
            max = sum
    else:
        dfs(L+1, sum+scores[L], hour+hours[L])
        dfs(L+1, sum, hour)


if __name__ == "__main__":
    n, m = map(int, input().split())

    scores = list()
    hours = list()
    max = 0

    for i in range(n):
        score, hour = map(int, input().split())
        scores.append(score)
        hours.append(hour)

    dfs(0, 0, 0)
    print(max)

