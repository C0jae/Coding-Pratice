# 총 모험가 수
n = int(input("총 인원 : "))

# 모험가별 공포도
fear = list(map(int, input("공포도 : ").split()))

# 공포도를 오름차순 정렬
fear.sort()

# 한 팀에 들어갈 팀원 수
cnt = 0

# 총 팀 수
team = 0

for i in fear:
    # 팀원 수 + 1
    cnt += 1
    
    # 증가하는 팀원 수가 i(공포도) 이상이면 팀 하나 생성 
    # 새로운 팀 인원 산출을 위해 cnt = 0으로 초기화
    if (cnt >= i):
        team += 1
        cnt = 0
        
print("총 팀 :", team, "팀")