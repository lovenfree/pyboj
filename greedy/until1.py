target, num = map(int, input().split())
count=0

while True:
    if(target%num==0):
        target=target//num
    else:
        target -=1
    count += 1
    if target ==1:
        break


print(count)
