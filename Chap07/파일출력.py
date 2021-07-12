# 파일 출력하기
fhand = open('mbox.txt')
count = 0
for line in fhand:          # 파일 안의 줄을 세는방법 변수 line은 각 줄 당 한번씩 루프를 돈다 
    count = count + 1       # 새로운 줄을 만날 때마다 변수에 1을 더해줌
print('Line Count: ', count)

# 앞부분에 From:이 들어간 줄을 찾아내는 방법 >> 이 경우에는 개행문자까지 전부 출력되는 형태이다(원래 파일 안의 개행문자) 
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswitch('From:'):   # From: 으로 시작하는 줄을 출력 
        print(line) # print함수의 개행문자 => 총 개행문자가 한 라인에 2개씩 존재

# 파일 안의 개행문자 제거하기
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()    # 개행문자는 출력되지 않는 공백문자이므로 rstrip으로 지울 수 있음 (오른쪽 끝에서부터 공백문자를 지움)
    if line.startswitch('From:'):
        print(line) # print함수의 개행문자로 라인이 하나 넘어갈 때마다 줄 바꿔짐

# 파일안에 여러 줄이 있고 그 중 특정한 줄을 출력하고 싶을 때
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswitch('From:'):   # 줄이 From:으로 시작하지 않으면,
        continue                        # 생략해버림
    print(line)

# 특정한 문장을 출력하는 방법
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()            # 공백제거
    if not '@uct.ac.za' in line:    # @uct.ac.za가 해당 줄에 없다면,
        continue                    # 생략해버림(그 다음 줄로 넘어감)
    print(line)


# 유동적으로 파일을 선택해서 받고 싶을 때
fname = input('Enter the file name : ') # 값을 받는 input구문 사용
try:    # 잘못된 파일명이 들어왔을때의 예외처리
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()  # 실행되면 아무것도 반환하지 않음

count = 0   # 파일 줄을 세기 위한 변수
for line in fhand:  # 라인 줄을 세기 위한 반복문
    if line.startswitch('Subject: '):   # 처음이 Subject: 로 시작하면
        count = count + 1   # 해당 단어가 들어있는 줄의 갯수를 세줌
print('There were', count, 'subject lines in', fname)
