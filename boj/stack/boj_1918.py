import sys
def input(): return sys.stdin.readline().rstrip()


state = input()
stack = list()


def precedence(ch):
    if ch == '(':
        return 0
    if ch in '+-':
        return 1
    return 2


result = ''
for i in state:
    if 'A' <= i <= 'Z':
        result += i
        # print("##" + result)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        while stack:
            op = stack.pop()
            # print(""+op)
            if op == '(':
                break
            result += op
            # print("##2" + result)
        # stack.pop()
    else:
        while stack and precedence(stack[-1]) >= precedence(i):
            result += stack.pop()
            # print("##3" + result)
        stack.append(i)

    # for j in stack:
    #     print(j, end=' ')
    # print()


while stack:
    result += stack.pop()
print(result)
