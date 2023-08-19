import sys

sys.stdin = open("input.txt","r")

def dfs(L):
    global answer

    if L==size:
        cha = max(ch)-min(ch)
        if answer > cha:
            temp = set()
            for x in ch:
                temp.add(x)
            if len(temp) == 3:
                answer = cha
    else:
        for i in range(loop):
            ch[i]+=numbers[L]
            dfs(L+1)
            ch[i] -= numbers[L]

if __name__ == "__main__":
    size = int(input())
    loop = 3

    numbers = list()
    for i in range (size):
        numbers.append(int(input()))

    answer = 999999999
    ch = [0]*loop
    dfs(0)
    print(answer)
