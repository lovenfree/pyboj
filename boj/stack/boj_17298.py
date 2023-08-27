import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
stack = []
ans = [-1]*n

for i in range(n):
    if len(stack) == 0 or nums[stack[-1]] > nums[i]:
        stack.append(i)
    elif nums[stack[-1]] < nums[i]:
        # big number
        while len(stack) > 0 and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]
        stack.append(i)

print(' '.join(map(str, ans)))
