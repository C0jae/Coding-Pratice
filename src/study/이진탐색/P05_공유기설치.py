n, c = list(map(int, input("집, 공유기 개수 : ").split()))

# 전체 집의 좌표 정보 입력받기
array = []
for _ in range(n):
    array.append(int(input("집 좌표 : ")))

array.sort()

start = 1 # 가능한 최소거리
end = array[-1] - array[0] # 가능한 최대거리
result = 0

while(start <= end):
    mid = (start + end) // 2
    
    value = array[0]
    count = 1
    
    # 현재의 mid값을 이용해 공유기 설치
    for i in range(1, n): # 앞에서부터 설치
        if array[i] >= value + mid:
            value = array[i]
            count += 1
        
        # c개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
        if count >= c:
            start = mid + 1
            # 최적의 결과 저장
            result = mid
        # c개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        else:
            end = mid - 1

print(result)