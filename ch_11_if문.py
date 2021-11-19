# @Date       : 21.11.17(수) 22:14
# @Author     : ymkim
# @Contents   : IF문 파이썬

'''
IF문 파이썬
1. Scanner sc = new Scanner(System.in)을 사용하여 사용자 입력값 받음
2. 파이썬은 input() 키워드 사용하여 입력값을 받는다
'''

# 날씨 묻는 예제
# weather = input("오늘 날씨는 어떄요? ")

# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

temp = int(input("기온은 어떄요? "))

if temp > 30 : 
    print("너무 더워요, 나가지 마세요.")
elif 10 <= temp and temp < 30 :
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10 : 
    print("외투를 챙기세요.")
else:
    print("너무 추워요, 나가지 마세요.")