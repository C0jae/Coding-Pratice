def solution(n, arr1, arr2):
    answer = []
    arr1_bn = []
    arr2_bn = []
    
    # 배열의 10진법을 2진법으로 교체 - bin()
    # 2진법 표시로 같이 출력되는 b0 삭제 - [2:]
    # n자리수까지 표시(빈자리는 0으로 표시) - rjust()
    for i in range(n):
        arr1_bn.append(bin(arr1[i])[2:].rjust(n, "0"))
        arr2_bn.append(bin(arr2[i])[2:].rjust(n, "0"))
    
    # 두 배열중 하나라도 1인 값이 있다면 "#", 아니라면 " " 로 표시 후 결과값 answer.append
    for i in range(n):
        result = ''
        for j in range(n):
            if (arr1_bn[i][j] == "1" or arr2_bn[i][j] == "1"):
                result += "#"
            else:
                result += " "   
        answer.append(result)
    
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 221, 17, 28]

print(solution(n, arr1, arr2))
