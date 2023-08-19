def DFS(x):
    if x ==0:
        return

    DFS(x-1)
    print(x)

if __name__ == "__main__":
    DFS(3)