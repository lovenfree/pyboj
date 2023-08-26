import sys
input  = sys.stdin.readline

n=int(input())
A = list(map(int, input().split()))
NGE=[-1]*n
stack = list()

for i in range(n):
    if len(stack) == 0:
        stack.append(i)
    else :
        while len(stack)>0:
            if A[stack[-1]] < A[i]:
                t = stack.pop()
                NGE[t] = A[i]
            elif A[stack[-1]] > A[i]:
                t = stack.append(i)


print(NGE)

