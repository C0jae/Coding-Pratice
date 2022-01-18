# 문자열 s 입력받음과 동시에 리스트화 및 오름차순 정렬(sorted())
s = sorted(list(input("문자열 입력 : ")))

# 알파벳과 숫자를 분리할 변수 a, b 선언
a = ""
b = 0

# 아스키코드 이용하여 대문자 알파벳은 a에 추가, 숫자는 b에 +
for i in range(len(s)):
    if (ord(s[i]) >= 65 and ord(s[i]) <= 90):
        a += s[i]
    
    else:
        b += int(s[i])

# b가 하나라도 존재할 경우 a 와 b를 같이 출력
if b != 0:
    print(a + str(b))

# b가 하나도 없을 경우 정렬된 a만 출력
else:
    print(a)




# 답지풀이
data = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in data:
    # 알파벳일 경우
    if x.isalpha():
        result.append(x)
    
    # 숫자일 경우
    else:
        value += int(x)
        
    # 알파벳을 오름차순으로 정렬
    result.sort()
    
    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))
    
    # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
    print(''.join(result))