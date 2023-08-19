import sys

sys.stdin = open("input.txt","r")

def dfs(L,S):
    global count

    if L== len(chars):
        count+=1
        for j in range(S):
            print(chr(res[j]+64))
    else:
        for i in range(1,27):
            if chars[L]==i:
                res[S] =1
                dfs(L+1,S+1)
            elif i >=10 and chars[L]==i/10 and chars[L]%10 :
                res[S] = i
                dfs(L+2,S+1)
    print()

if __name__=="__main__":
    chars = list(map(int,input()))
    chars.insert(len(chars), -1)

    res = [0]*10
    count=0
    dfs(0,0)
    print(count)


