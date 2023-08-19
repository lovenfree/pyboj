import sys
sys.stdin = open("5_input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

si, ei = 0, 1
c = 0
sum = a[si]

while True:
    if sum == m:
        sum -= a[si]
        si += 1
        c += 1
    elif sum > m:
        sum -= a[si]
        si += 1
    elif sum < m:
        if ei < n:
            sum += a[ei]
            ei += 1
        else:
            break

print(c)
