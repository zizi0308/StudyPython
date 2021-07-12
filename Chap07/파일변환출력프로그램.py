# 텍스트 파일안에 있는 문자를 모두 대문자로 변환해서 출력하는 프로그램

fh = open('mbox-short.txt')

for line1 in fh:
    line2 = line1.rstrip()
    print(line2.upper())    # 문자변수인 line2, upper이 대문자로 문자를 변환
    
