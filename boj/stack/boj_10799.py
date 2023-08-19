import sys
input = sys.stdin.readline

pipes = list(input().strip())

stack = []
cnt = 0
for i in range(len(pipes)):
    if pipes[i] == '(':
        stack.append(i)
    elif pipes[i] == ')':
        last = stack[-1]
        if last == i-1:
            # Laser
            stack.pop()
            cnt += len(stack)
            # print("Laser : ", i, cnt)
        else:
            # pipe
            stack.pop()
            cnt += 1
            # print("Pipe : ", i, cnt)

print(cnt)
