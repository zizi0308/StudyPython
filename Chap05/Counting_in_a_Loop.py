# Counting in a Loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1         # 코드가 실행된 횟수
    print(zork, thing)
print('After', zork)

# Summing in a Loop
zork = 0
print('Before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)


# 평균
count = 0
sum = 0
for thing in [9, 41, 12, 3, 74, 15] :
    count = count + 1
for thing in [9, 41, 12, 3, 74, 15] :
    sum = sum + thing

print('After',sum, count, sum / count)


# 20보다 큰 값 찾기
num = 0
for thing in [9, 41, 12, 3, 74, 15] :
    if thing > 20:
        print('Large_num : ', thing)

# How to Find Smallest value
smallest = None         # None 타입 자료형(공백을 나타내기 위해 사용) >> None은 상수임
print('Before', smallest_so_far)

for the_num in [9, 41, 12, 3, 74, 15] :
    if smallest is None:        # smallest가 공백을 나타낼 때(is는 ==보다 더 강력한 연산자 >> None 자료형에만 사용하기) 참이되어 실행
        smallest = the_num      # smallest에 the_num 배열의 첫번째 값을 넣음(배열 첫번째 값을 복사)
    elif the_num < smallest:    # the_num에 들어있는 값보다 smallest에 들어있는 값이 더 클 때
        smallest = the_num      # smallest에 the_num에 들어있는 값을 대입(더 작은 값을 넣는다)
    print(smallest, the_num)
print('After', smallest)
