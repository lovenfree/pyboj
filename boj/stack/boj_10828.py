import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    cmd = input()
    size = len(stack)
    if cmd.startswith("push"):
        _, x = cmd.split()
        x = int(x)
        stack.append(x)

    elif cmd.startswith("top"):
        if size == 0:
            print(-1)
        else:
            print(stack[size-1])
    elif cmd.startswith("size"):
        print(size)
    elif cmd.startswith("pop"):
        if size == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd.startswith("empty"):
        if size == 0:
            print(1)
        else:
            print(0)
