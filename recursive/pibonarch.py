def pibo(i):
    if i ==1:
        return 1
    elif i ==2:
        return 1
    else :
        return pibo(i-1)+pibo(i-2)

print(pibo(7))