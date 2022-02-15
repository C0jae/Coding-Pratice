# 첫번째 인덱스 구하기
def first(array, x, start, end):
    if start > end:
        return None
    
    # 중간지점 mid
    mid = (start + end) // 2
    
    # 해당값을 가지고 있는 원소중에 가장 왼쪽 인덱스만 변환
    if mid == 0 or array[mid - 1] < x and array[mid] == x:
        return mid
    
    # 해당값이 중간지점보다 작거나 같을경우 m - 1 번째 까지로 인덱스 변환하여 다시 구하기
    elif array[mid] >= x:
        return first(array, x, start, mid - 1)
    
    # 해당값이 중간지점보다 클 경우 m + 1 번째 부터 인덱스 변환하여 다시 구하기
    else:
        return first(array, x, mid + 1, end)


# 끝지점 인덱스 구하기    
def last(array, x, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    # 해당값을 가지고 있는 원소중에 가장 오른쪽 인덱스만 변환
    if mid == n - 1 or array[mid + 1] > x and array[mid] == x:
        return mid

    # 해당값이 중간지점보다 작을경우 끝지점을 m - 1번째로 변환하여 다시 구하기
    elif array[mid] > x:
        return last(array, x, start, mid - 1)
    
    # 해당값이 중간지점보다 크거나 같을경우 시작지점을 m + 1번째 부터 변환하여 구하기
    else:
        return last(array, x, mid + 1, end)


# 답 구하기
def solution(array, x, start, end):
    n = len(array)
    
    # 해당값의 첫번째 인덱스
    a = first(array, x, 0, n - 1)
    
    # 해당값이 없다면 0 리턴
    if a == None:
        return 0
    
    # 해당값의 마지막 인덱스
    b = last(array, x, 0, n - 1)
    
    # 해당값의 총 갯수 구하기
    return b - a + 1


n, x = map(int, input("n, x 입력 : ").split())

array = list(map(int, input("n 리스트 입력 : ").split()))

cnt = solution(array, x)

if cnt == 0:
    print(-1)

else:
    print(cnt)
    

def solution(array, x):
    count = 0
    
    for i in array:
        if i > x:
            break
        
        elif i == x:
            count += 1
    
    return count