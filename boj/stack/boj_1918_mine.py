import sys
def input(): return sys.stdin.readline().rstrip()


state = input()
stack = list()

state = list(state)

idxA = ord('A')
idxZ = ord('Z')

result = ''
for i in state:
    if idxA <= ord(i) <= idxZ:
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
        else:
            # 연산자
            while len(stack) > 0 and (i == '+' or i == '-') and ((stack[-1] == '/' or stack[-1] == '*') or (stack[-1] == '+' or stack[-1] == '-')):
                result += stack.pop()
            stack.append(i)
        # while (i == '+' or i == '-') and (stack[-1] == '/' or stack[-1] == '*') and (stack[-1] == '+' or stack[-1] == '-'):
        #     result += stack.pop()
        # stack.append(i)
else:
    while len(stack) > 0:
        result += stack.pop()

print(result)
