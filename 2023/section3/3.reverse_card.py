import sys
sys.stdin = open("3_input.txt", "rt")

# a = [0]*21

a = list(range(21))
# print(a)

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

print(a[1::])
