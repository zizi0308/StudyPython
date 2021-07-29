# 딕셔너리를 활용한 데이터 빈도수 측정

# When we see a new name

counts = dict()             # 빈 dictionary생성
names = ['csev', 'cwen', 'csev', 'ziqian', 'cwen']
for name in names:          # 반복변수 name
    if name not in counts:  # 딕셔너리의 Key로 존재하지 않을때
        counts[name] = 1    # 값(value)을 1로해서 새로하나 추가함
    else:                   # 이미 존재한다면,
        counts[name] = counts[name] + 1 # 해당 키값을 받아와서  1을 더한 후 집어넣음
print(counts)   # 히스토그램 출력


# The get method for dictionaries  # counts.get(name, 0) + 1 << 관용적인 코드

# 위와 같은 식을 get 함수를 통해 간결화 할 수 있음
x = counts.get(name, 0)
counts = dict() 
names = ['csev', 'cwen', 'csev', 'ziqian', 'cwen']
for name in names: 
    counts[name] = counts.get(name, 0) + 1  # 여기서 0은 디폴트 값 딕셔너리에 새로운 대상을 만들어 넣음
print(counts)   
