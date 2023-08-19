import sys
sys.stdin = open("3_input.txt")


def dfs(level, sum):
    global res
    if level==n:
        if sum>0 and sum<=t:
            res.add(sum)

    else:
        dfs(level+1,sum+weights[level])
        dfs(level+1,sum-weights[level])
        dfs(level+1,sum)
    
    
if __name__=="__main__":
    n = int(input())
    weights = list(map(int,input().split()))
    t = sum(weights)
    res=set()
    dfs(0,0)
    print(t-len(res))
