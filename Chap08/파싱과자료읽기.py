fhand = open('mbox-short.txt')
for line in fhand:          # 한줄 씩 이동을 위한 for문
    line = line.rstrip()    # 개행문자 제거
    #print('Line: ', line)
    wds = line.split()
    #print('Words: ',wds)
    # Guardian a bit stronger
    if len(wds) < 3 or wds[0] != 'From':    # 연산자 쓸때는 순서가 중요함(앞부분이 참이면 뒤는 그냥 넘기기 때문)
        continue            # From으로 시작하지 않는 라인은 생략
    print(wds[2])

