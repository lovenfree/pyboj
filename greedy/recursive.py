def recursive_fun(i):
    if i==10:
        return
    print(i, '재귀함수를 호출합니다.')
    recursive_fun(i+1)
    print(i, '이건 아래에 있어요 재귀함수를 종료합니다.')

recursive_fun(0)