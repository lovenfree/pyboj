def dfs(L,S):
    if L==count:
        print(ch)
        return

    for i in range(S,size+1) :
        ch[L] = i
        dfs(L+1,i+1)




if __name__ == "__main__":

    size = 4
    count =2
    ch = [0]*2
    dfs(0,1)