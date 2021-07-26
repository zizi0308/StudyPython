a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

t = [9, 41, 12, 3, 74, 15]
t[1:3]
t[:4]
t[3:]
t[:]

# Buliding a List from Scratch
stuff = list()  # 생성자 형태, list()라는 명령어로 빈 리스트 생성이후 이를 변수 stuff에 할당 
stuff.append('book')    # append : 리스트 삽입함수
stuff.append(99)
print(stuff)

# Is Somthing is a List? >> in연산자 사용시, list안에 존재하면 True, 아니면 False
some = [1, 9, 21, 10, 16]
9 in some   # True
15 in some  # False
20 not in some  # True

# List are in Order
friends = ['Lee', 'Kim', 'Choi']
friends.sort()
print(friends)
print(friends[1])   # 정렬된 순서로 리스트값이 재배치 됨


# Bulid-in Functions and Lists >> 리스트를 입력으로 하는 여러가지 함수
nums = [3, 41, 144, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))  # 평균을 구하는 함수


# 1.
total = 0
count = 0
while True: 
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1

avg = total / count
print('Average: ', avg)

# 2 더 많은 메모리를 차지
numlist = list()    # 변수 numlist에 할당된 빈 리스트
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)   # 바로 연산하는 1과는 달리, 값을 리스트에 추가

average = sum(numlist) / len(numlist)
print('Average: ', average)
