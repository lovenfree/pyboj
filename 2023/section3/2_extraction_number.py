import sys
sys.stdin = open("input_2.txt", "rt")

c = input()
n = ""
for i in c:
    if i.isdigit():
        n += i

number = int(n)
print(number)
divisor = 0
for i in range(1, number+1):
    if number % i == 0:
        # print(i, end=' ')
        divisor += 1
print(divisor)
