def dfs(L):
    if L==size:
        print(ch)
        return


    for i in range (1, number+1):
            if dup[i]!= 0:
                continue
            ch[L] = i
            dup[i] = 1
            dfs(L+1)
            dup[i]=0


if __name__ == "__main__":
    number =3
    size = 2
    ch = [0]*size
    dup = [0]*(number+1)
    dfs(0)