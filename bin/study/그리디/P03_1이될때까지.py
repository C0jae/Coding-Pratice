# n, k값 입력
n, k = map(int, input("n, k값 입력 : ").split())

# 실행횟수 변수 선언
cnt = 0;

# n값이 1이 될때까지 무한반복
while n != 1:
    # n이 k의 배수가 아니라면 n = n - 1 진행 및 cnt +1
    if (n % k != 0):
        n -= 1
        cnt += 1
    
    # n이 k의 배수일 경우 n = n / k 진행 및 cnt +1
    else:
        n /= k
        cnt += 1
        
print(cnt)