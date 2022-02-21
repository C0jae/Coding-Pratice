def solution(height, m, start, end):
    # 시작점이 끝점을 넘게되면 종료
    while start <= end:
        # 중간지점 길이 설정
        mid = (start + end) // 2
        # 남는 떡의 길이 변수 설정
        result = 0
        
        for i in height:
            # 떡의 길이가 mid 이상일 경우 넘는 수치만큼 +
            if i > mid:
                result += i - mid
        
        # 전체 남는 길이가 요청길이 초과일 경우 시작지점 이동(증가)
        if result > m:
            start = mid + 1
        
        # 전체 남는 길이가 요청길이 미만일 경우 끝점 이동(감소)
        elif result < m:
            end = mid - 1
        
        # 남는길이와 요청길이가 같은경우 해당 지점 리턴
        else:
            return mid
    
    return None

n, m = list(map(int, input("떡 개수 및 요청한 떡의 길이(n, m) : ").split()))
height = list(map(int, input("떡의 개별 높이").split()))
height.sort()

# 각 떡의 길이변수, 요청길이, 시작지점, 끝지점(가장 긴 떡의 길이)
a = solution(height, m, 0, height[n - 1])

# None이 이날경우 해당값 출력
if a != None:
    print(a)

# None일 경우 만들 수 없음(길이부족)
else:
    print("만들 수 없다.")