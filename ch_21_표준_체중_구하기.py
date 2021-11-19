# @Date       : 21.11.18(목) 13:01
# @Author     : ymkim
# @Contents   : 표준 체중을 구하는 프로그램을 작성하시오

# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# 💣 내가 작성한 예제 ex01)
def std_weight(height, gender) :
    standard_weight = 0
    height = float(height) / 100 # 키(m) 구하기
    print(height)
    if gender == "남자" :
        standard_weight = height * height * 22
    elif gender == "여자" :
        standard_weight = height * height * 21
    else :
        print("성별을 잘못 입력하셨습니다. 다시 시도해주세요.")
    print(standard_weight)
    print(round(standard_weight, 2))

    return round(standard_weight, 2)

# height = input("키를 입력해주세요 : ")
# gender = input("성별을 입력해주세요 : ")
# standard_weight = std_weight(height, gender)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, standard_weight))

# 💣 내가 작성한 예제 ex02)
def std_weight_t(height, gender = "남자") :
    height = int(height) / 100
    is_height_type = (type(height) == float)
    is_height_range = True if height > 0 and height < 250 else False

    print(gender)

    std_weight = 0
    if is_height_type == True and is_height_range == True :
        if gender == "남자" :
            std_weight = height * height * 22
        elif gender == "여자" :
            std_weight = height * height * 21
        else :
            print("Error In!")
    else :
        print("Error Out!")

    return round(std_weight, 2)

height = input("키 : ")
gender = input("성별 : ")
std_weight = std_weight_t(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, std_weight))

# 🚀 개발자분이 작성한 예제
def std_weight_p(height, gender) :
    if gender == "남자" :
        return height * height * 22
    else :
        return height * height * 21

height = 175
gender = "남자"
weight = std_weight_p(height / 100, gender)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))