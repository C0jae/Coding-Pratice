def binary_search(array, target, start, end):
    while start <= end:
        # 중간점 구하기
        mid = (start + end) // 2
        
        # 중간점이 찾으려는 수일 경우 해당 변수 반환
        if array[mid] == target:
            return mid
    
        # 중간점이 target보다 클 경우 중간점 왼쪽으로 범위 축소 
        elif array[mid] > target:
            end = mid - 1
        
        # 중간점이 target보다 작을경우 중간점 오른쪽으로 범위 축소
        else:
            start = mid + 1
    
    return None
    

# 주어진 단어
array = ["jin", "nara", "winter", "spring", "summer"]

# 찾을 단어 입력
target = input("찾을 단어 입력 : ")

# 단어 정렬
array.sort()

# binary_search 함수 적용
result = binary_search(array, target, 0, len(array) - 1)

if result == None:
    print("원소가 존재하지 않습니다.")

else:
    print(result + 1)