n = int(input("총 부품 갯수 : "))
nc = list(map(int, input("부품 종류 : ").split()))
# 정렬
nc.sort()

m = int(input("요청 부품 갯수 : "))
mc = list(map(int, input("요청 부품 종류 : ").split()))
# 정렬
mc.sort()

# n의 범위만큼 부품 존재여부 파악하는 리스트 생성
data = [0] * 1000001

# 현재 보유한 부품의 data 자리는 1로 변경
for i in range(len(nc)):
    data[nc[i]] = 1
    
result = ""

# 찾는 부품의 자리와 data의 리스트 자리를 비교하여 1이면 yes, 0이면 no를 출력
for i in range(len(mc)):
    if data[mc[i]] == 1:
        result += "yes "
    
    else:
        result += "no "

print(result)

#####################################################################################################################

# 함수설정(존재하는 부품, 찾는부품, 시작인덱스, 끝 인덱스)
def solution(nc, target, start, end):
    # 시작이 끝점을 넘어갈 경우 종료
    while start <= end:
        # 중간지점 위치 찾기
        mid = (start + end) // 2
        
        # 찾는 부품이 중간지점일경우
        if nc[mid] == target:
            return mid
        
        # 중간지점보다 작을경우
        elif nc[mid] > target:
            end = mid - 1
        
        # 중간지점보다 클경우
        else:
            start = mid + 1
        
        return None
    
for i in mc:
    result = solution(nc, i, 0, n - 1)
    
    if result != None:
        print("yes", end = " ")
        
    else:
        print("no", end = " ")
        
print(result)