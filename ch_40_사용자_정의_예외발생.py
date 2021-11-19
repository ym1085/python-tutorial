# @Date       : 21.11.18(목) 21:11
# @Author     : ymkim
# @Contents   : 사용자 정의 예외 발생 시키기

'''
1. Custom Exception Class를 생성
2. Clean Code에서 Exception 처리할때가 있었음
'''

class BigNumberError(Exception) :
    
    # msg = ""

    # 메시지를 넣고 싶다면
    def __init__(self, msg) :
        self.msg = msg

    def __str__(self) :
        return self.msg    

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : ")) 
    num2 = int(input("두 번째 숫자를 입력하세요 : ")) 
    
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 출력을 원하는 메시지 입력 
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError : 
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력해주세요.")
    print(err) # Error 발생 시 msg 내용 출력

