
# Sorting Lists of Tuples

d = {'a':10, 'c':1, 'b':22}
print(d.items())

print(sorted(d.items()))    # 순서가 엉망일때 sorted함수 사용 (시퀀스를 받아서 정렬한 뒤에 리턴)

# Using sorted()

d = {'a':10, 'c':1, 'b':22}
t = sorted(d.items())
