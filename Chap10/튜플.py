# 튜플과 리스트의 차이를 이해하고, 튜플의 특성을 활용해 문제를 해결할 수 있다

# Tuples are like lists
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 9, 2)
print(max(y))

# but,,, Tuples are "immutable" >> 리스트는 변경가능, 튜플은 한 번 만들면 정렬만 가능
# 그냥 값을 저장하고 접근만 할 거라면, 튜플이 더 효율적임(list에서 쓰는 함수는 튜플에서 거의 못씀)
x = [9, 8, 7]
x[2] = 4
print(x)

y = 'ABC'
# y[2] = 'D' # error    << 얘는 당연히 에러

z = (5, 4, 3)
# z[2] = 0  # !!error!! << 리스트는 수정가능하지만 튜플은 에러남 
# Line14와 비슷하다고 생각하면됨 튜플은 뭉텅이로 있는 것

# Tuples and Assingnment >>  좌변에 변수를 가진 채로 선언 가능
# 튜플을 좌변에 놓을 수 있음 >> 다시 말해, 함수가 튜플을 리턴할 수도 있다는 것
(x , y) = (2, 'fred')       # 대신 좌변 개수와 우변의 개수는 같아야 함
print(y)

# Tuples and Dictionaries
# 딕셔너리에 튜플을 뽑아서 튜플로 이루어진 리스트를 정렬(딕셔너리를 리스트로 바꾸고 리스트정렬)
d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k, v) in d.items():    # 딕셔너리 안에 있는 key가 없을 때까지 튜플에 할당
    print(k, v)

tups = d.items()    # 일종의 튜플로 이루어진 리스트 클래스
print(tups)

# Tuples are Comparable << 튜플 안의 값에 대한 비교가 가능함 
(0, 1, 2) < (5, 1, 2)   # True >> 첫번째의 비교가 참이될 때, 바로 True가 나온다
('Jones', 'Sally') > ('Adams', 'Sam') # True (l과 m의 차이에 의해)

