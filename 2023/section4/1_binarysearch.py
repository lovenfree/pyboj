import sys
sys.stdin = open("1_input.txt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

# 이분검색
# lt, rt, mid = (lt+rt//2)

a.sort()
# print(a)

lt = 0
rt = n-1
mid = (lt+rt)//2

# if a[mid]


while (True):

    # print(lt, rt, mid)
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid-1
        mid = (lt+rt)//2

    elif a[mid] < m:
        lt = mid+1
        mid = (lt+rt)//2

# for i in range(len(a)):
#     if a[i] == m:
#         print(i+1)
#         break
