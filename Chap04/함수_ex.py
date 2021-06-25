# 이전에 적었던 급여계산 프로그램을 함수를 써서 다시 작성해보기

def paycalc(hour, rate):
    print("급여계산기 시작")


hour = input('일한 시간을 입력하세요: ')
rate = input('당신의 시급을 입력하세요: ')
h = float(hour)
r = float(rate)
paycalc(hour, rate)

if h > 40:          # 조건이 복잡한 식이 if로 오게하고 나머지 쉬운 식은 else로 빼는게 좋음
    reg = h * r
    otp = (h - 40) * (r * 0.5)
    res1 = reg + otp
    print("당신의 급여는 초과급여", otp,"원을 포함해서 ", res1, "원 입니다.")
else:
    res2 = h * r
    print("당신의 급여는 ", res2, "입니다.")
