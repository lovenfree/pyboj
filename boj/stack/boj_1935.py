import sys
def input(): return sys.stdin.readline().rstrip()


n = int(input())
str = input()

alist = list()
state = list(str)
stack = list()
for _ in range(n):
    alist.append(int(input()))

for i in state:

    if i != '*' and i != '/' and i != '+' and i != '-':
        stack.append(alist[ord(i)-65])
    else:
        r = stack.pop()
        l = stack.pop()

        v = 0.00
        if i == '*':
            v = r*l
        elif i == '/':
            v = l/r
        elif i == '+':
            v = l+r
        elif i == '-':
            v = l-r
        stack.append(v)
print('%.2f' % stack[-1])
