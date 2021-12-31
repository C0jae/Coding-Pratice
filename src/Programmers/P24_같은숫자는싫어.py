def solution(arr):
    answer = []
    
    # 첫번째 수 할당(연속여부를 판단할 필요가 없음)
    answer.append(arr[0])
    
    # 두번째 값부터 전의 값과의 연속성 여부 판단하여 할당
    for i in range(1, len(arr)):
        if (arr[i] != arr[i - 1]):
            answer.append(arr[i])
    
    return answer

arr = [1, 1, 3, 3, 0, 1, 1]
print(solution(arr))