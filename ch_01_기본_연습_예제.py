# @Date       : 21.11.17(수) 16:47
# @Author     : ymkim
# @Contents   : 파이썬 기본 문법 및 차이점 비교하면서 지식 습득

# Number Type
print("*********Int*********")
print( 5 )
print( -10 )
print( 3.14 )
print( 1000 )
print( 5 + 3 )
print( 2 * 8 )
print( 3 * ( 3 + 1 ) )

###########
print("\n")
print("*********String*********")

# String Type
print( '풍선' ) # 작은 따옴표
print( "나비" ) # 큰 따옴표
print( "ㅋㅋㅋㅋㅋㅋㅋㅋㅋ" )
print( "ㅋ" * 9 ) # 문자열 + 숫자( 반복횟수 )

###########
print("\n")
print("*********Boolean*********")

# Boolean Type
print( 5 > 10 )
print( 5 < 10 )
print( True)  
print( False )
print( not True )     # ! : not 연산자를 저런식으로 사용
print( not False )    # True, False도 대문자로 사용이 되는 듯
print( not ( 5 > 10 ) ) # FALSE -> TRUE

###########
print("\n")
print("*********변수 사용 실습*********")

# Variable
# Q. Introduce your pet
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print( "우리집 " + animal + "의 이름은 " + name + "에요" )
print( name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요" )
print( name + "는 어른일까요? " + str(is_adult) )

###########
print("\n")
print("*********문제 풀이*********")

'''
파이썬 주석
1. #
2. ''' '''
3. ?
'''

# Q. 변수를 이용하여 다음 문장을 출력하시오
#   변수명 
#     : station
#   변수값 
#     : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장
#     : XX행 열차가 들어오고 있습니다.

# A. 문제 답안
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

###########
print("\n")

# A. 문제 답안 Loop 사용
stationList = [ "사당", "신도림", "인천공항" ]
for station in stationList:
    print(station + "행 열차가 들어오고 있습니다.")

###########
print("\n")
print("*********연산자 실습*********")
print( 1 + 1 )      # 2
print( 3 - 2  )     # 1
print( 5 * 2 )      # 10
print( 6 / 3 )      # 2

print(( 3 > 0 ) and ( 3 < 5 ))
print(( 3 > 0 ) or ( 3 < 2 ))

print( 2 + 3 + 4 )
print( (2 + 3 ) * 4)
number = 2 + 3 + 4      # 9
print("number = " + str(number))
number = number + 2     # 11
print("number = " + str(number))
number += 3             # 14
print("number = " + str(number))

###########
print("\n")
print("*********랜덤 함수 실습*********")

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성

print("\n")

print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 미만의 임의의 값 생성

print("\n")
print("*********로또 값 6번 출력*********")
print(int(random() * 45) + 1);
print(int(random() * 45) + 1);
print(int(random() * 45) + 1);
print(int(random() * 45) + 1);
print(int(random() * 45) + 1);

print("\n")
print("*********randrange 함수 사용*********")
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

print("\n")
print("*********실습 퀴즈*********")

# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1) 랜덤으로 날짜를 뽑아야 한다
# 조건2) 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3) 매월 1~3일은 스터디 준비를 해야 하므로 제외

# 월 4회
#     - 온라인 : 3번
#     - 오프라인 : 1번
#     - 매월 : 1~3일 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.

random = (int(random() * 29) + 4)
random = randint(4, 28) # radint는 시작값(포함), 끝값(포함)이다
print("오프라인 스터디 모임 날짜는 매월 " + str(random) + "일로 선정되었습니다.");

print("\n")
print("*********문자열 실습*********")

sentence = "나는 소년입니다"
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

print("\n")
print("*********슬라이싱*********")

jumin = "930823-1065627" # 문자열 잘라서 가져온다
print("성별 : " + jumin[7])      # index
print("연 : " + jumin[0 : 2])     # N - N 직전까지 출력 
print("연 : " + jumin[2 : 4])     # N - N 직전까지 출력 
print("월 : " + jumin[4 : 6])

print("월 : " + jumin[: 6]) # 처음부터 N 직전까지
print("월 : " + jumin[7 : 14]) # 처음부터 N 직전까지
print("뒤 7자리 : " + jumin[-7:]) #


