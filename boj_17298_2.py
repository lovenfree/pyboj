import sys
input  = sys.stdin.readline

n=int(input())
A = list(map(int, input().split()))
NGE=[-1]*n
stack = list()

for i in range(n):
    if stack.count == 0:
        stack.append(i)
    else:
        t = stack[-1]
        while stack.count>0:
            if A[t] < A[i]:
                t = stack.pop()
                NGE[t] = A[i]
            elif A[t] > A[i]:
                t = stack.append(i)


print(NGE)

