# 딕셔너리를 활용해 데이터 빈도수 측정
fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = dict() # 생성자형태로 dictinary 생성
for line in handle:
    line = line.rstrip()
    # print(line)
    words = line.split()
    # print(words)
    for w in words:
        # di라는 딕셔너리에 대해 get method가 첫번째 매개변수로 key값인 w를 변수로 받고, 
        # 딕셔너리에 존재하지 않는 값은 0으로 처리 (if not there the count is zero)
        # 1번 방법
        # oldcount = di.get(w, 0)
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1     # 새로운값이 들어오면 원래있던 값에 1을 더해줌
        # di[w] = newcount
        # print(w, 'new', newcount)
        
        # 2번 방법 : 관용적으로 쓰이는 표현 (위의 내용을 다 포함한) >> 카운터(vlaues)를 검색하고, 새로만들고, 업데이트 함
        di[w] = di.get(w, 0) + 1    # 이 키가 가진 예전 값이나 0을 가져와서 1을 더함

print(di)


# now we want to find the most common word >> 딕셔너리에 루프적용

#bigcount = None
#bigword = None

#for word, count in di.items():
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count

#print(bigword, bigcount)

largest = -1    # 통상적으로 value는 양수값이므로 초깃값을 -1로 설정해주면 편함
for k, v in di.items():
    if v > largest:
        largest = v
        theword = k

print('Done', theword, largest)



