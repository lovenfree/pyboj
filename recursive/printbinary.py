def printbinary(x):
    if x==0:
        return
    else:
        printbinary(x//2)
        print(x%2, end=' ')

printbinary(11)