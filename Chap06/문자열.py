# 일반적으로 while 루프와 for루프 모두를 사용할 수 있고, 그 외 조건이 같을 때 for 사용

fruit = 'banana'
for letter in fruit:
    print(letter)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


word = 'banana'
count = 0
for letter in word:     # 문자열 banana의 각 문자에 대해 변수 letter의 값을 특정문자로 바꾸면서 루프실행
    if letter == 'a':
        count = count + 1
print(count)

# Slicing String << 마지막 인덱스는 포함하지 않는다.

s = 'Monty Python'
print(s[:2])    # Mo        >> 처음부터 2번전까지
print(s[8:])    # thon      >> 8번째부터 마지막까지
print(s[:])     # Monty Python >> 처음부터 끝까지


a = 'Hello'
b = a + 'There'
print(b)     # HelloThere
c = a + ' ' + 'There'
print(c)     # Hello There


# in 논리연산자(for문에 쓰는 것과는 다른 형태임) >> bool값 반환
fruit = 'banana'
'n' in fruit    # True (Visual Studio에서는 적용 안됨, 파이썬에서는 실행됨)
'm' in fruit
if 'a' in fruit:
    print('Found it!')

# 문자열 비교

if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana')
else:
    print('All right, bananas.')

## 문자열 라이브러리

# 소문자 변환함수 .lower() (함수에 매개변수를 전달하는 것이 아닌 !객체.함수이름!을 적는 것으로 일어나는 함수호출) >> 객체지향 함수라고도 함
# 메소드는 기본적으로 기존의 문자열을 바꾸지 않고 원본문자열을 복사해서 사용함
greet = 'Hello Bob'
zap = greet.lower()     
print(zap)
print(greet)
print('Hi There'.lower()) # 문자열에 대한 소문자변환

# 문자열을 찾는 함수 .find()

fruit = 'banana'
pos = fruit.find('na')  # 찾은 문자의 개수를 출력
print(pos)

aa = fruit.find('z')    # 찾은 문자열이 없을 시 -1 반환
print(aa)

# 문자열을 찾거나 대체하는 함수(search / replace)

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)

# 문자열 공백을 없애는 함수 .strip()
greet = '  Hello Bob   '
greet.lstrip()      #'Hello Bob   '
greet.rstrip()      #'  Hello Bob'
greet.strip()       #'Hello Bob' >> 양쪽 모두의 공백을 없앰

# 문자열 파싱하기
data = 'From stephen.marquard@uct.ac.za Sat Jan   5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)