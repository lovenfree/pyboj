def printnumber(i):
    if i==0:
        return
    printnumber(i-1)
    print(i)

printnumber(3)