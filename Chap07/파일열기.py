# Reading File

# Using Open >> open(파일명, 파일을 읽을지 쓸지 선택하는 모드)
# handle = open(Filename, mode)   
# # open 함수가 파일 핸들을 반환, 지정한 변수인 handle에 저장

xfile = open('mbox.txt')    # 파일을 열고 파일핸들을 받음 이 파일 핸들은 데이터가 아니고 순서임
for cheese in xfile:        # for문으로 파일안의 텍스트를 하나하나씩 읽음
    print(cheese)
