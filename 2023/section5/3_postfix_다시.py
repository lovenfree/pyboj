import sys
sys.stdin = open("3_input.txt", "rt")

str = input()
# str = list(str)
stack = []
result = ""


for i in str:
    if i.isdecimal():
        result += i
    else:
        if i == "+" or i == "-":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.append(i)
        elif i == "*" or i == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                result += stack.pop()
            stack.append(i)
        elif i == "(":
            stack.append(i)
        elif i == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()

while stack:
    result += stack.pop()


print(result)
