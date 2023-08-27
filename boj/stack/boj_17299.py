import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
FREQ = dict()
NGF = [-1]*n

for i in A:
    try:
        FREQ[i] += 1
    except:
        FREQ[i] = 1

stack = list()

for i in range(n):
    while (len(stack) > 0 and FREQ[A[stack[-1]]] < FREQ[A[i]]):
        t = stack.pop()
        NGF[t] = A[i]

    stack.append(i)

for i in range(n):
    print(NGF[i], end=' ')
