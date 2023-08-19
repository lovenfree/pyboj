import sys
sys.stdin = open("2_input.txt", "rt")

str = input()
str = list(str)

stack = []
cnt = 0

for i in str:
    if i == "(":
        stack.append(i)
    elif i == ")" and stack and stack[-1] == "(":
        stack.pop()
        cnt += len(stack)
    elif i == ")" and stack and stack[-1] == ")":
        stack.pop()
        cnt += 1
print(cnt)
