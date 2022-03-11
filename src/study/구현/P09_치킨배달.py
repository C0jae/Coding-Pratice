from itertools import combinations


# 크기 n, 최소 치킨가게 수 m 입력
n, m = map(int, input("크기 n, 치킨가게 수 m : ").split())

field = []  # 도시의 집 및 치킨가게 정보 리스트
store = [] # 치킨가게 좌표정보
home = []  # 집 좌표정보

# field에 집과 치킨가게 정보입력
for i in range(n):
    field.append(list(map(int, input("도시정보 입력 : ").split())))

    # 집과 치킨가게의 좌표를 찾아 각각 저장
    for j in range(n):
        if field[i][j] == 1:
            home.append((i, j))
        
        elif field[i][j] == 2:
            store.append((i, j))

# 치킨가게 중 m개의 조합 리스트 구하기
ncr = list(combinations(store, m))

# 치킨거리의 합 구하기
def check(ncr):
    result = 0
    
    # 집의 좌표
    for x, y in home:
        length = int(1e9)
        
        # 치킨가게의 좌표
        for a, b in ncr:
            # 치킨 가게별로 집과의 길이를 구한 후 최소거리로 적용
            length = min(length, abs(x - a) + abs(y - b))
        
        # 모든 치킨거리를 더하기
        result += length
    
    # 치킨거리의 합 리턴
    return result

result = int(1e9)

# 치킨가게가 위치할 수 있는 모든 경우의 수
for i in ncr:
    # 해당 경우의 수마다 리턴되는 치킨거리의 합 중 최소값을 식별
    result = min(result, check(i))

print(result)