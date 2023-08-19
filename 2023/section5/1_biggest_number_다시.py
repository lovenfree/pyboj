import sys
sys.stdin = open("1_input.txt", "rt")

number, cnt = input().split()
number = list(map(int, str(number)))
cnt = int(cnt)
stack = []

# print(number)
n = 0


for i in number:
    while stack and cnt > 0 and stack[-1] < i:
        stack.pop()
        cnt -= 1
    stack.append(i)

if cnt != 0:
    stack = stack[:-cnt]

print(stack)
print(''.join(map(str, stack)))
