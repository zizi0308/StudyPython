# 반복문

# while문
while True: # True는 상수 참값이 됨
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break       # 가장 안쪽에 있는 루프에서 루프의 마지막줄 다음으로 빠져나옴
    print(line)
print('Done!')

# for문
friends = ['Jo', 'Kim', 'Han']
for friend in friends:          # friends 배열에 있는 friend들을 출력함
    print("Happy New Year!", friend)
print('Done')
