
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
tmp = sorted(tmp, reverse=True) # 키가 아닌 값 순서대로 정렬함 >> reverse=True로 큰값부터 정렬
print(tmp)

