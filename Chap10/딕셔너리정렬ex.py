
# 파일 불러들인 후 가장 많이 나온 단어 5개 정렬하기

fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt' # 그냥 엔터쳤을때
hand = open(fname)                      # 파일오픈

di = dict()             # 딕셔너리 생성
for lin in hand:        # 줄을 읽고
    lin = lin.rstrip()  # 한줄로
    wds = lin.split()   # 공백따라 단어를 띄우고
    for w in wds:       # 단어를 쪼개서
        di[w] = di.get(w, 0) +1 # 키-값 쌍을 만들어줌
# print(di)


tmp = list()            # 리스트 선언
for k,v in di.items():
# print(k, v)
    newt = (v, k)       # 키-값순으로 정렬된 값을 값 - 키순으로 바꿔줌
    tmp.append(newt)    # 튜플로 만들어줌
# print('Flipped', tmp)

tmp = sorted(tmp, reverse = True)   # 내림차순으로 정렬
#print('Sorted', tmp[:5])
for v, k in tmp[:5]:    # 처음부터 5번째까지 정렬
    print(k,v)          # 키 - 값 순으로 출력