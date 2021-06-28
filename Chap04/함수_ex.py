# 이전에 적었던 급여계산 프로그램을 함수를 써서 다시 작성해보기

def paycalc(hour, rate):
    # print("급여계산기 실행", hour, rate) # 디버깅용

    if hour > 40:          # 조건이 복잡한 식이 if로 오게하고 나머지 쉬운 식은 else로 빼는게 좋음
        reg = hour * rate
        otp = (hour - 40) * (rate * 0.5)
        pay = reg + otp
        return pay
    else:
        pay = hour * rate
        return pay


hour = input('일한 시간을 입력하세요: ')
rate = input('당신의 시급을 입력하세요: ')
h = float(hour)
r = float(rate)         # 입력이 일어난 후

xp = paycalc(h, r)      # 함수 호출

print("총 급여 : ", xp) # 해당 함수 출력







        
