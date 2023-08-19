import sys
sys.stdin = open("1_input.txt", "rt")

n, m = map(int, input().split())

a = list()
for i in range(1, n):
    if n % i == 0:
        a.append(i)

print(a[m-1])
