import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
NGE = [-1]*n
stack = list()

for i in range(n):
    if len(stack) == 0:
        stack.append(i)
    else:
        while len(stack) > 0 and A[stack[-1]] < A[i]:
            # if A[stack[-1]] < A[i]:
            t = stack.pop()
            NGE[t] = A[i]
            # elif A[stack[-1]] > A[i]:
            #     break
        stack.append(i)

for i in range(n):
    print(NGE[i], end=' ')
