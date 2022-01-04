n = int(input("동전 갯수 입력 : "))
coin = list(map(int, input("화폐단위 입력 : ").split()))

# 결과값 result 1로 정의
# 가장 작은 화폐가 2원 이상일 경우 for문을 바로 빠져나와 1의 값을 출력하기 위해
result = 1

# 화폐단위 오름차순 정렬
coin.sort()

for i in coin:
    # 왜 result가 이 조건을 만족할때가 정답인지 모르겠음
    if i > result:
        break
    
    result += i

print(result)
        