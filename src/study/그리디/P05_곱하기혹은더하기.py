s = list(map(int, input("입력 : ")))

# 결과값 result 변수 선언
result = 0

for i in range(len(s)):
    # 계산 순서중 0이 있을경우 +, 없을경우 x 진행
    if (s[i] == 0 or result == 0):
        result += s[i]
    
    else:
        result *= s[i]
        
print(result)