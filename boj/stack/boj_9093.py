# import sys
# input = sys.stdin.readline
# t = int(input())
# for _ in range(t):
#     s = input()
#     stack = []
#     for ch in s:
#         if ch == ' ' or ch == '\n':
#             print(''.join(stack[::-1]), end='')
#             stack.clear()
#             print(ch, end='')
#         else:
#             stack.append(ch)

import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = input()
    stack = []

    for t in s:
        if t == " " or t == '\n':
            print(''.join(stack[::-1]), end='')
            # for _ in range(len(stack)):
            #     print(stack.pop(), end='')
            stack.clear()
            print(t, end='')
        else:
            stack.append(t)
