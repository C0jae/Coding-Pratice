n, m = map(int, input("n, m 입력 : ").split())

# 최단경로를 나타내는 data 리스트 생성(초기값 INF)
INF = int(1e9)
data = [[INF] * (n + 1) for _ in range(n + 1)]

# 연결된 헛간끼리 이동거리 1로 설정
for i in range(m):
    a, b = map(int, input("연결된 헛간 번호 입력 : ").split())
    data[a][b] = 1
    data[b][a] = 1

# 같은장소의 이동거리 0으로 설정
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            data[i][j] = 0

# 플로이드 워셜 알고리즘 실행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            data[i][j] = min(data[i][j], data[i][k] + data[k][j])

# 초기값 기준 : 1번방 -> 2번방으로의 정보
num = 2                 # 방(헛간) 번호
distance = data[1][2]   # 이동거리
cnt = 1                 # 동일한 거리의 헛간 수

# 2번방 기준의 변수가 정해져 있으므로 3번방서부터 탐색
for i in range(3, n + 1):
    # 이동거리가 같다면 cnt +1 후 다음 헛간 탐색
    if data[1][i] == distance:
        cnt += 1
        continue
    
    # 이동거리가 INF보다 작고(이동경로가 있을때) 이전까지의 탐색한 이동거리보다 길때
    # 새로운 이동거리 및 헛간 번호설정
    # 동일한 거리의 헛간 수 1로 초기화
    if data[1][i] < INF and data[1][i] > distance:
        distance = data[1][i]
        num = i
        cnt = 1
        
print(num, distance, cnt)