이진검색/ 이분탐색

정렬이 되어 있다
값이 특정 범위에 있다
절반식 줄인다
탐색범위 ( lt, rt, mid)


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    

#phthond의 이진 탐색 라이브러리
bisect_left(a,x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스
bisect_right(a,x): 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스



Parametric(모수)) binary_search

이진 탐색을 사용해야 하는 문제가 나오는 것

파라메트릭 서치 : 최적화 문제를 결정 문제("예"/"아니오") 로 바꾸어 해결하는 기법
: 특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는다

일반적으로 코딩 테스트에서 파라메트릭 서치는 이진 탐색을 이용하여 해결할 수 있다.
