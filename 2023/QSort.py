def Qsort(lt,rt):
    if lt<rt:

   

        #pos 는 제자리를 찾음
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)



if __name__=="__main__":
    arr=[45,21,23,36,15,67,11,60,20,33]
    print("Before sort: ", end='')
    print(arr)
    Qsort(0,7)
    print()
    print("After sort: ",end=' ')
    print(arr)