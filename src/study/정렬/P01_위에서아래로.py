from audioop import reverse


n = int(input("수의 개수 n : "))
result = []
for i in range(n):
    result.append(int(input("수 입력 : ")))

# 내림차순 정렬
result.sort(reverse=True)

for i in result:
    print(i, end=" ")