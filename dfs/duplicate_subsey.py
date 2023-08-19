import sys

def dfs(L):
    global  cnt
    if L==size:
        # for i in range(0,size):
        cnt+=1
        print(ch)
        return

    for i in range(1,number+1):
        ch[L] = i
        dfs(L+1)


if __name__ =="__main__":
    number = 3
    size = 2
    cnt = 0
    ch = [0]*size
    dfs(0)
    print(cnt)

