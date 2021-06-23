# Variables, Expressions, Statement
# 파이썬은 문자로 시작한 다음, 문자, 숫자, 밑줄(_)로 변수의 이름을 정함
# 연산 시 우선 순위 : 괄호 > 거듭제곱 > 나누기 곱하기(같이 있으면 왼쪽부터 오른쪽으로) 
# > 더하기 빼기

#대입문
#nam = input('Who are you? ')    # 입력받음(string 값을)
#print('Welcome', nam)           # 입력받은 값을 출력


# 사용자가 일한 시간과 시급을 프롬프트에 입력시, 임금을 계산하는 프로그램

hour = input('일한 시간을 입력하세요: ')
h = float(hour)     # string을 float으로 형변환
rate = input('당신의 시급을 입력하세요: ')
r = float(rate)
print('당신의 임금은 ',h * r,' 입니다')