# done이 입력되기 전까지 반복해서 숫자를 물어보고 합계를 출력하고 마지막에 평균도 냄(에러처리도 함)
# 잘못된 값 입력시 무효한 입력값이라고 출력한뒤 계속 실행

num = 0
total = 0.0

while True:                                 # 무한반복 루프
    sval = input('숫자를 입력하세요 : ')    # 문자열을 입력받기 위한 변수생성
    if sval == 'done':                      # 문자열이 'done'일 경우 종료
        break
    try:
        fval = float(sval)                  # 문자열을 숫자열로 변환(문자열이 입력될 시 예외처리)
    except:
        print('Isvalid Input')              # 예외처리시 출력할 문자열
        continue                            # 잘못된 입력을 막기위해 다시 맨 위로 돌아가서 실행                            
    #print(fval)
    num = num + 1                           # 코드가 실행된 횟수
    total = total + fval                    # 입력받은 숫자들의 합 계산

#print('All Done')
print(total, total / num)                   # 총 합계 및 평균값 출력 
    
    
    
   
