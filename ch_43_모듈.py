# @Date       : 21.11.19(금) 10:00
# @Author     : ymkim
# @Contents   : 모듈(Module)

'''
1. 모듈이란 필요한 것들끼리 모여있는 파일
2. 자동차
    - 타이어 교체
    - 범퍼 교체
    - 부품만 교체할 수 있도록 틀은 잡는다
'''

# 영화 극장이 존재
# 신용카드는 받지 않고, 현금만 받는다
# 잔돈을 반환해주지 않는다
# 즉, 정확히 35000원을 딱 맞춰서 내야 한다

def price(people) :
    print("{0} 명 가격은 {1}원 입니다.".format(people, people * 10000)) # 사람 수, 영화 가격

def price_morning(people) :
    print("{0} 명 조조 할인 가격은 {1}원 입니다.".format(people, people * 6000)) # 사람 수, 영화 가격

def price_soldier(people) :
    print("{0} 명 군인 할인 가격은 {1}원 입니다.".format(people, people * 4000)) # 사람 수, 영화 가격


