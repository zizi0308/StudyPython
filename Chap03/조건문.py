#파이썬은 코드블락 없이 들여쓰기로 구분하므로 주의해서 쓸 것!(spacebar x4 = tap)
# if, elif, else 조건문은 순서가 중요하다(순차적으로 조건을 비교하기 때문)

# 사용자가 일한 시간과 시급을 프롬프트에 입력시, 임금을 계산하는 프로그램
# 40시간 이상일 경우 초과근무(시급의 1.5배)

hour = input('일한 시간을 입력하세요: ')
rate = input('당신의 시급을 입력하세요: ')
h = float(hour)
r = float(rate)

#if h <= 40:
#    res1 = h*r
#    print("당신의 급여는 ", res1, "입니다.")  
#else:
#    res2 = (h-40) * (r*1.5) + (h*r)
#    print("당신의 급여는 초과급여를 포함해서 ", res2, "입니다.")  
    
if h > 40:          # 조건이 복잡한 식이 if로 오게하고 나머지 쉬운 식은 else로 빼는게 좋음
    reg = h * r
    otp = (h - 40) * (r * 0.5)
    res1 = reg + otp
    print("당신의 급여는 초과급여", otp,"원을 포함해서 ", res1, "원 입니다.")
else:
    res2 = h * r
    print("당신의 급여는 ", res2, "입니다.") 

  
    