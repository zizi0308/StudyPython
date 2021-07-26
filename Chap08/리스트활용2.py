# Best Friends: Strings and Lists
abc = 'With three words'
stuff = abc.split() # 공백을 기준으로 문자열을 여러조각으로 나누어 각각의 분리된 리스트를 생성
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)


line = 'A lot       of spaces'
etc = line.split()  # 공백이 있어도 알아서 예쁘게 나눠줌
print(etc)
line = 'first;second;third'
thing = line.split()    # split안에 아무것도 없다면, 공백을 기준으로 리스트를 분리
print(thing)
print(len(thing))
thing = line.split(';') # 리스트 안에 있는 ;을 기준으로 분리
print(thing)
print(len(thing))

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()    # 개행문자 제거
    if not line.startswith('From ') : continue  # From으로 시작하는 줄만 찾아냄
    words = line.split()    # 연결된 문장을 공백을 기준으로 쪼개 리스트로 생성
    print(words[2])          # 선택된 라인 중 2번째 위치에 있는 단어만 찾아내 출력
    
# The Double Split Pattern  << 분할한 결과를 새로운 규칙을 정해 재분할 하는 경우
# 이메일 뒷부분을 찾고자 할 때 find, pose의 작업 외의 또 다른 방법 split
#  이메일 예시 : From stephen.marquard@uct.ac.za Sat Jan 6 09:14:16 2008
words = line.split()
email = words[1]    # stephen.marquard@uct.ac.za
pieces = email.split('@')   # ['stephen.marquard', 'uct.ac.za']
#print(pieces[1])    # 'uct.ac.za'
