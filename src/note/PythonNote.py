# 무작위로 위치한 리스트 array
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    # 첫번째 원소 피벗으로 설정
    pivot = array[0]
    
    # 피벗을 제외한 리스트 설정
    tail = array[1:]
    
    # 피벗 이하의 원소들을 리스트 분할
    left_side = [x for x in tail if x <= pivot]
    
    # 피벗보다 큰 원소들을 리스트 분할
    right_side = [x for x in tail if x > pivot]
    
    # 분할 이후 왼쪽부분과 오른쪽 부분에 대해 각각 정렬 수행 및 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)