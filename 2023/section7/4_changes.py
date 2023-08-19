import sys
sys.stdin = open("4_input.txt","rt")

def dfs(L,sum):
    global cnt

    if sum>t:
        return
    
    if L== k:
        if sum == t:
            cnt+=1
    else:

        for i in range(numbers[L]+1):
            dfs(L+1, sum+(i*moneys[L]))


if __name__=="__main__":
    t = int(input())
    k = int(input())

    moneys = list()
    numbers = list()

    for i in range(k):
        m,n = map(int, input().split())
        moneys.append(m)
        numbers.append(n)  
    cnt=0
    dfs(0,0)
    print(cnt)                                                     