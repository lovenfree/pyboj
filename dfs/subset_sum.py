import sys


def dfs(v,sum):
    if v == n:
        if total//sum == 2:
            print("YES")
            sys.exit(0)
    else:
        dfs(v+1,sum+array[v])
        dfs(v+1,sum)

if __name__ =="__main__":

    array=[1,3,5,6,9,10]

    n= len(array)
    total = sum(array)
    dfs(0,0)
    print("NO")