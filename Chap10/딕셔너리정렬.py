
# Sorting Lists of Tuples

d = {'a':10, 'c':1, 'b':22}
print(d.items())

print(sorted(d.items()))    # 키의 순서가 엉망일때 sorted함수 사용 (시퀀스를 받아서 정렬한 뒤에 리턴)

# Using sorted()

d = {'a':10, 'c':1, 'b':22}
t = sorted(d.items())

[('a', 10), ('c', 1), ('b', 22)]
for k, v in sorted(d.items()):  # d.items()에서 가져오기 전에 sorted를 사용해 정렬
    print(k, v) # 이것 또한 키값 순으로 정렬된 값이 나옴

# Sort by values instead of key >> 키가 아닌 값으로 정렬하기
c = {'a' : 10, 'b' : 1, 'c' : 22}
tmp = list() # 리스트를 넣을 임시 공간생성   
for k, v in c.items(): 
    tmp.append((v, k)) # 튜플로 된 리스트 >> 값이 처음, 키가 뒤에 나오는 형태(순서를 뒤집음)
print(tmp)
tmp = sorted(tmp, reverse=True) 
# sorted 함수는 리스트가 어떻게 만들어졌는지 상관없이 튜플로 된 리스트가 있다면 각 튜플의 첫번째 원소로 정렬
# reverse=True로 큰값부터 정렬
print(tmp)

# 가장 많이 나오는 단어 10개 뽑아보기
fhand = open('romeo.txt')   # 파일오픈
counts = dict()     # 딕셔너리 생성
for line in fhand:  # 파일 읽기 (한 줄씩 루프들 돌고,)
    words = line.split()    # 공백제거
    for word in words:  # 단어읽기 (한줄 안의 한단어들에 대해 반복문을 돈다)
        counts[word] = counts.get(word, 0) +1   # 히스토그램만들기
# print(counts) >> 단어별 개수만 세고있음(정렬 X)

lst = list() # 리스트 생성(순서를 구하기 위해서)
for key, val in counts.items(): # 튜플로 된 리스트생성(키, 값 형태)
    newtup = (val, key) # 생성된 튜플을 값, 키 형태로 저장
    lst.append(newtup)  # 저장한 것을 리스트에 추가함

lst = sorted(lst, reverse=True) # 내림차순 정렬(sort함수는 튜플 중 첫번째에 해당되는 것으로 정렬함)
# print(lst) >> 값-키 형태의 출력(큰 수부터)

for val, key in lst[:10] :  # 앞에서 10번째 튜플까지 슬라이싱
    print(key, val)         # 슬라이싱한 튜플을 다시 키-값 형태로 바꿔서 출력

# Even Shorter Version
c = {'a':10, 'b':1, 'c':22}
# sorted는 리스트를 입력값으로 받고,
# []안의 부분을 list comprehension 이라고 부름(파이썬에게 리스트라고 이야기해주는 부분)
# 리스트가 두 개 짜리 튜플로 만들어져있다(v, k) 그러니 c.times()에 있는 모든 k,v에 대해 for루프처럼 반복하게 되고 리스트를 생성
# 다른 변수나 값의 저장 없이 쭉 리스트를 만들어 냄
print( sorted( [ (v, k) for k, v in c.items() ], reverse=True))



