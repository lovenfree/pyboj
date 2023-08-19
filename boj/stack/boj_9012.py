import sys
input = sys.stdin.readline


n = int(input())

for _ in range(n):
    stack = []
    s = list(input())

    # print(s)
    for x in s:
        # print(s[x], end='-')
        if x == '(':
            stack.append(x)
        elif x == ')':
            # print(stack[-1])
            if len(stack) == 0:
                print('NO')
                break
            elif stack[-1] == ')':
                print('NO')
                break
            else:
                stack.pop()
    else:

        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
