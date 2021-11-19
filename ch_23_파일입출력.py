# @Date       : 21.11.18(목) 14:4
# @Author     : ymkim
# @Contents   : 파일 입출력

'''
1. 실행할 경우 파일 생성되는 부분 체크
2. 기존에 있는 파일 제거 후 테스트 해볼 것
'''

# @ open("파일명", "읽기 타입", "인코딩 타입")
score_file = open("score.txt", "w", encoding="utf-8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 새롭게 파일 작성
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 파일 읽어오기
score_file = open("score.txt", "r", encoding="utf8") # 읽기
print(score_file.read())
score_file.close()

# 파일 한줄한줄 읽어와서 처리
score_file = open("score.txt", "r", encoding="utf-8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
score_file.close()

# 파일이 몇줄인지 모르는 경우
score_file = open("score.txt", "r", encoding="utf-8")
while True :
    line = score_file.readline()
    if not line :
        break
    print(line)
score_file.close()

# List형태로 파일 받아와서 저장후 출력
score_file = open("score.txt", "r", encoding="utf-8")
lines = score_file.readlines()
for line in lines :
    print(line, end="")

score_file.close()
