# 순차탐색 소스코드 구현

# 주어진 단어
array = ["jin", "nara", "winter", "spring", "summer"]

# 찾을 문자열 입력
target = input()

# 각 원소를 하나씩 확인
for i in range(len(array)):
    if array[i] == target:
        print(i + 1)
        break