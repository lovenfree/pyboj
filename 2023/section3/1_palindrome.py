import sys
sys.stdin = open("1_input.txt", "rt")

n = int(input())

for i in range(n):
    c = input().lower()
    size = len(c)
    # for x in range(size//2):
    #     if c[x] != c[-1-x]:
    #         print("#%d NO" % (i+1))
    #         break
    # else:
    #     print("#%d YES" % (i+1))
    if c == c[::-1]:
        print("#%d YES" % (i+1))
    else:
        print("#%d NO" % (i+1))
