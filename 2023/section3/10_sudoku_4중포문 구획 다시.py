import sys
sys.stdin = open("input_10.txt", "rt")


def solve(a):
    ch = [0]*10
    ch2 = [0]*10

    # 행
    for i in range(9):
        for j in range(9):
            ch[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch) != 9 | sum(ch2) != 9:
            print("NO")
            return

    # 구획
    for x in range(0, 9, 3):
        print("++++++=")
        for i in range(x, x+3):
            for j in range(3):
                print(i, j)
                ch[a[i][j]] = 1
        if sum(ch) != 9:
            print("NO")
            return
    print("YES")


# a = list()
# for _ in range(9):
a = [list(map(int, input().split())) for _ in range(9)]

solve(a)


# 구획
