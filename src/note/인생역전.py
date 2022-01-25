import random


tryCnt = 1
correct = 0

while correct < 1:
    print(tryCnt, "번째")
    
    result = [0] * 1000
    i = 0

    while i < len(result):
        a = []
        j = 0
        
        while j < 6:
            num = random.randrange(1, 46)
            
            if num not in a:
                a.append(num)
                j += 1
                
        a.sort()
        result[i] = a
        
        i += 1

    cntresult = [0] * len(result)

    for i in range(len(result)):
        cnt = 0
        
        for j in range(len(result)):
            if result[i] == result[j]:
                cnt += 1
        
        cntresult[i] = cnt

    for i in range(len(cntresult)):
        if cntresult[i] == 2:
            print(result[i], cntresult[i])
            correct += 1
    
    tryCnt += 1