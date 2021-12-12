#n, m값 입력
n, m = map(int, input("n, m값 입력 : ").split())

result = 0

for i in range(n):
    arr = list(map(int, input("카드값 입력 : ").split()))
    min_value = min(arr)
    
    if (min_value >= result):
        result = min_value

print(result)