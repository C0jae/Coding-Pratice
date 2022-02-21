def solution(number, start, end):
    # 문제조건에 일치하는 값이 없을경우
    if start > end:
        return None
    
    else:
        # 중간지점 선언
        mid = (start + end) // 2
        
        # 문제조건과 일치할 경우
        if number[mid] == mid:
            return mid

        # 문제조건과 일치하지 않을 경우
        else:
            if number[mid] > mid:
                return solution(number, start, mid - 1)
            
            else:
                return solution(number, mid + 1, end)
        
n = int(input("수 갯수 : "))
number = list(map(int, input("정수 정보 : ").split()))

if solution(number, 0, n - 1) == None:
    print(-1)
    
else:
    print(solution(number, 0, n - 1))