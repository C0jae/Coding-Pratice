# 가격, 돈, 탑승 횟수를 변수로 하는 solution 함수 생성
def solution(price, money, count):
    # 놀이기구 총 이용금액 변수(sum) 선언 및 정의
    sum = 0
    
    # 이용횟수가 n번째일때의 금액 (이용요금 * n번)을 산출하여 합산
    for i in range(count):
        sum += (i + 1) * price
    
    # n번 이용에 필요한 금액(sum) - 가지고 있는 돈(money) return
    if (sum >= money): return sum - money
    else: return 0

# 이용요금, 보유금액, 횟수 테스트 변수 선언 및 정의
price = 3
money = 20
count = 4

# 테스트 값 출력
print(solution(price, money, count))