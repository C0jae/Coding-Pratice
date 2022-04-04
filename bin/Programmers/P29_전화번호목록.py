def solution(phone_book):
    # 오름차순 정렬
    phone_book.sort()
    
    for i in range(len(phone_book) - 1):
        # i번째의 단어가 i + 1번째 단어에 앞부분에 존재할 경우 false 리턴
        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            return False
    
    # 위의 조건이 없었을 경우 true 리턴    
    return True

phone_book = ["123", "986123", "789"]

print(solution(phone_book))