# 파일에 저장된 데이터를 읽어와서 딕셔너리를 활용하여 데이터 빈도수를 측정

# 루프로 딕셔너리 만들기
#counts = dict()
#print('Enter a line of text: ')
#line = input('')

#words = line.split()

#print('Words: ', words)

#print('Counting...')
#for word in words:
#    counts[word] = counts.get(word,0) + 1
#print('Counts: ', counts)

# 딕셔너리 자체에 루프 적용하기
counts = {'chuck' : 1, 'fred' : 42, 'jan' : 100}    # key : value
for key in counts:
    print(key, counts[key])

# 키를 얻을 수 있는 방법
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(list(jjj))
print(jjj.keys())   # keys method    # key, value method 둘다 적어도 같은 순서로는 나옴(순차X)
print(jjj.values()) # values method
print(jjj.items())  # items method >> 원소를 직접물어봄 >> tuple 키,  값 쌍으로 리스트를 줌

# Two Iteration Variables
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
for aaa,bbb in jjj.items():
    print(aaa, bbb)

# 텍스트 파일을 받고 연 다음, 문장을 단어단위로 쪼개 그 단어에 대한 빈도수를 측정(히스토그램)
name = input('파일을 선택하세요 : ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# 위의 딕셔너리 중 가장 큰값을 가진 키와 쌍을 찾고 싶을 때
bigcount = None # 루프 초기화
bigword = None
for word,count in counts.item():    # 2개의 반복변수
    if bigcount is None or count > bigcount:    # 값이 없거나(처음 들어가는 값), 또는 이전 bigcount보다 클 때,
        bigword = word
        bigcount = count

print(bigword, bigcount)



