def solution(n, ball):
    # 결과값 선언
    cnt = 0
    
    for i in range(n):
        # range(i, n)을 통해 중복선택 방지
        for j in range(i, n):
            # 같은 무게의 볼링공 제외
            if (ball[i] != ball[j]):
                cnt += 1
    
    return cnt

# 값 입력
n, m = map(int, input("n, m 입력 : ").split())
ball = list(map(int, input("무게 입력").split()))

print(solution(n, ball))