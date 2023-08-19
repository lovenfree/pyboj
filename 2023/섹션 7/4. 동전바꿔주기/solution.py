import sys

sys.stdin = open("input.txt","r")

def dfs(L,sum):
    global count

    if sum > total:
        return

    if L==kinds:
        if sum == total:
            count+=1
            return
    else:
        for i in range(numbers[L]+1):
            dfs(L+1,sum+(moneys[L]*i))




if __name__ == "__main__" :

    total = int(input())
    kinds = int(input())

    moneys=list()
    numbers =list()


    for i in range(kinds):
        a,b  = map(int, input().split())
        moneys.append(a)
        numbers.append(b)
    count=0
    dfs(0,0)
    print(count)