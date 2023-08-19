import sys
sys.stdin = open("5_input.txt","rt")



def dfs(L):
    global res

    if L==N:
        gap = max(sums)-min(sums)
        if gap<res:
            temp = set()
            for x in sums:
                temp.add(x)
            if len(temp)==3:
                res  = gap
        
    else:
        for i in range(3):
            sums[i]+=nums[L]
            dfs(L+1)
            sums[i]-=nums[L]


if __name__=="__main__":
    N = int(input())
    nums=list()
    for i in range(N):
        nums.append(int(input()))
    sums=[0]*3
    res=9999999999
    dfs(0)
    print(res)