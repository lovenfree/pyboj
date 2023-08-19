import sys
from collections import deque
sys.stdin = open("7_input.txt", "rt")

max = 10000
ch=[0]*(max+1)
nums = [0]*(max+1)

if __name__ == "__main__":
    s, e = map(int, input().split())
    ch[s]=1
    nums[s]=0

    dQ = deque()
    dQ.append(s)

    while dQ:
        n = dQ.popleft()
        if n==e:
            break

        for i in (n-1,n+1,n+5):
            if i>0 and i<max and ch[i]==0:
                dQ.append(i)
                ch[i]=1
                nums[i]=nums[n]+1

    print(nums[e])        

    
