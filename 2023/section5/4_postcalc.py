import sys
sys.stdin = open("4_input.txt", "rt")

str = input()
stack = []
result = 0
for s in str:
    if s.isdecimal():
        stack.append(s)
    else:
        num1 = int(stack.pop())
        num2 = int(stack.pop())
        if s == "+":
            stack.append(num2+num1)
        elif s == "-":
            stack.append(num2-num1)
        elif s == "*":
            stack.append(num1*num2)
        elif s == "/":
            stack.append(num2/num1)

print(stack)
