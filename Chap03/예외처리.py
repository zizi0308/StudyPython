# traceback을 방지하기 위해 try-except문을 씀 try부분에서 에러가 났을 때 
# except가 실행되서 파이썬이 멈추는 것을 방지해줌

hour = input('일한 시간을 입력하세요: ')
rate = input('당신의 시급을 입력하세요: ')

try:
    h = float(hour)
    r = float(rate)
except:
    print("Error, 숫자를 입력해주세요")
    quit()

if h > 40:          
    reg = h * r
    otp = (h - 40) * (r * 0.5)
    res1 = reg + otp
    print("당신의 급여는 초과급여", otp,"원을 포함해서 ", res1, "원 입니다.")
else:
    res2 = h * r
    print("당신의 급여는 ", res2, "입니다.") 