# @Date       : 21.11.18(목) 11:24
# @Author     : ymkim
# @Contents   : continue, break

absent = [2, 5] # 결석 학생
no_book = [7] # 책을 깜빡함

for student in range(1, 11) :
    if student in absent :
        continue
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    
    print("{0}, 책을 읽어봐".format(student))
