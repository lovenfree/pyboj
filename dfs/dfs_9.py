import sys

def dfs(L):

    if L==num:
        total =0
        for j in range (0,num):
            total+=ch[j]*base[j]

        if total == 16:
            print(ch, total)
            sys.exit(0)

    for i in range(1, num+1):
        if dup[i]!=0:
            continue

        ch[L] = i
        dup[i] =1
        dfs(L+1)
        dup[i]=0

if __name__ == "__main__":
    sum = 16
    num =4
    dup = [0]*(num+1)
    base = [1]*num
    for i in range (1,num-1):
        base[i]=num-1
    ch = [0]*4
    dfs(0)