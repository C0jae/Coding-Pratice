a = input("문자열 a : ")
b = input("문자열 b : ")

n = len(a)
m = len(b)

# 각 인덱스까지의 편집 최소값을 나타내는 리스트 선언
dp = [[0] * (m + 1) for _ in range(n + 1)]

# i행 0열 초기값 설정
for i in range(n + 1):
    dp[i][0] = i

# 0행 i열 초기값 설정    
for i in range(m + 1):
    dp[0][i] = i

# 그냥 외우기(공식?)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 문자가 같으면 리스트 내에서 왼쪽 위에 해당하는 수 그대로 입력
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        
        # 문자가 다를경우 왼쪽위, 왼쪽, 위쪽 중 최소값 + 1로 입력
        else:
            dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

print(dp[n][m])