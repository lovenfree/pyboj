def dfs(n,sum):
    global max

    if sum > weigth:
        return
    if n==size:
        if sum>max:
                max=sum

    else:
        dfs(n+1,sum+weigths[n])
        dfs(n+1, sum)


if __name__ =="__main__":
    max=0
    weigth = 259
    size =5
    weigths=[81,58,42,33,61]
    dfs(0,0)
    print(max)

