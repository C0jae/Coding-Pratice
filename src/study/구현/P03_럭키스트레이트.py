n = list(map(int, input("점수 입력 : ")))

# 왼쪽 및 오른쪽 자릿수 점수 합 변수 선언
l = 0
r = 0

# n배열의 길이 변수 선언
s = len(n)

for i in range(s):
    # 왼쪽부분 점수 산출
    if (i < s/2):
        l += n[i]
    
    # 오른쪽 부분 점수 산출
    else:
        r += n[i]

if (l == r):
    print("LUCHY")

else:
    print("READY")