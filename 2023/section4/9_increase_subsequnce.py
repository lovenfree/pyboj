import sys
from collections import deque
sys.stdin = open("9_input.txt", "rt")

n = int(input())
l = list(map(int, input().split()))
# l = deque(a)

s = ""

lt = 0
rt = len(l)-1
last = 0
s = ""

while lt <= rt:
    lv = l[lt]
    rv = l[rt]

    print(lv, rv, last, s)
    if lv > last or rv > last:
        if lv < rv:
            s += "L"
            last = l[lt]
            lt += 1
        elif rv < lv:
            s += "R"
            last = l[rt]
            rt -= 1
    elif lv < last and rv < last:
        break


print(len(s))
print(s)
