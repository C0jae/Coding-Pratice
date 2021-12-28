import math

s = list(map(int, input("문자열 s 입력 : ")))

# 문자열의 숫자가 다를때마다 카운트 증가
cnt = 0;

for i in range(len(s) - 1):
    # i번째 수와 i + 1 번째 수를 비교해서 다르면 cnt + 1
    if (s[i] != s[i + 1]):
        cnt += 1

# 변경될 때마다 카운트가 증가하였으므로 카운트 / 2
# cnt가 홀수일경우(s[0] != s[len(s)]) cnt / 2 의 반올림       
result = math.ceil(cnt/2)

print(result)