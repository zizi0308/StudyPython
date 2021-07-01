# string 문자 파싱하기
# 문자열 잘라서 숫자만 float으로 형변환 시켜서 출력하기

str = 'X-DSPAM-Confidence: 0.8475'

str1 = str.find(':')
print(str1)

num = str[str1+2 :]
print(num)

fval = float(num)

print(fval)
print(fval + 42.0)