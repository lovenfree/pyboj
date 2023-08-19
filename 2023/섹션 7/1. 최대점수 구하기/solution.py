import sys
sys.stdin = open("in1.txt","r")

def dfs(L,sum, time):
    global max
    if time > limittime:
        return

    if L == size:
        if sum > max:
            max = sum
    else:
        # for i in range (L,size):
        #     if dup[i] != 1:
        #         dup[i] = 1
        dfs(L+1,sum+scores[L], time+times[L])
        dfs(L + 1, sum, time)
                # dup[i] =0

if __name__=="__main__":
    size, limittime = map(int, input().split())

    scores=list()
    times=list()

    for i in range(size):
        a,b = map(int, input().split())
        scores.append(a)
        times.append(b)
    max =0
    dfs(0,0,0)
    print(max)