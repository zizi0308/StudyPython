# A Story of Two Collections(인덱싱하는 방법에서 차이가 발생함)
# List : 연속적으로 착착 쌓여있는 것(프링글스통 안의 감자칩)
# Dictionary : 순서없이 그냥 있음 대신 키 존재(가방안에 있는 물건들인데 라벨이 붙어있음)

# Dictionaries
purse = dict()
purse['money'] = 13     # money가 13에 부여하는 라벨이 됨, 12가 딕셔너리에 놓임
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

print(purse['candy'])   # 인덱스 연산자를 출력

purse['candy'] = purse['candy'] + 2     # 딕셔너리의 내용을 업데이트
print(purse)

# Comparing Lists and Dictionaries
# 1. list의 Key는 방의 번호(int)이다
lst = list()
lst.append(21)
lst.append(183)
print(lst)

lst[0] = 23         # 원래 있는 위치값을 통해 값을 바꿈
print(lst)

# 2. doctionary의 key는 문자열(다른 것도 가능)이다. 
ddd = dict()
ddd['age'] = 21
ddd['course'] = 183
print(ddd)

ddd['age'] = 23     # 'age'라는 인덱스를 통해서 값을 바꿈
print(ddd)

# Dictionary Literals(중괄호안에 키, 콜론, 값이 연속으로 들어가있음)
jjj = {'chuck' : 1, 'fred' : 42, 'jan' : 100}
print(jjj)
ooo = {}
print(ooo)