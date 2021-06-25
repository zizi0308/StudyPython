# def는 코드를 생성하여 기록함 <<  저장단계

# 내장함수 >> python이 가지고 있는 함수
big = max('Hello world')
print(big)


# 사용자 정의함수 << 함수를 호출해야 실행
def greet(lang):        # 매개변수 lang
       if lang == 'es':
           print('Hola')
       elif lang == 'fr':
            print('Bonjour')
       else:
           print('Hello')

greet('en')     # 어떤언어로 호출하는지는 함수 호출때 쓰면됨
greet('es')
greet('fr')

def welcome():
    return "Nice to meet you"   # 반환도 매개변수로 간주함

print(welcome(), "Sara")
print(welcome(), "Jun")