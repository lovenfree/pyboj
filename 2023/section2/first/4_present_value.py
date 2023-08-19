import sys
sys.stdin = open("input_4.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
# sum = 0
# for i in a:
#     sum += i

avg = round(sum(a)/n)

d = float('inf')
result = 0
value = 0


for idx, x in enumerate(a):
    t = abs(x-avg)
    if t < d:
        result = idx
        d = t
        value = x
    elif t == d & value < x:
        result = idx
        d = t
        value = x
    elif t == d & value == x:
        continue

# for i in range(len(a)):
#     t = a[i]-avg

#     if abs(t) < d:
#         result = i
#         d = abs(t)
#         value = a[i]
#     elif abs(t) == d & value < a[i]:
#         result = i
#         d = abs(t)
#         value = a[i]
#     elif abs(t) == d & value == a[i]:
#         continue

print(avg, result+1)
