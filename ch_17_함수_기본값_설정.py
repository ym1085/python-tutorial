
# @Date       : 21.11.18(목) 12:23
# @Author     : ymkim
# @Contents   : 함수 기본값 설정

# def profile(name, age, main_lang) :
#     print("이름 : {0}\t 나이 : {1}\t 사용 언어 : {2}" \
#         .format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")


# 같은 학교 같은 학년 같은 반 같은 수업
# default value를 TypeScript처럼 적용해두는 것 같다
def profile(name, age = 17, main_lang = "파이썬") :
    print("이름 : {0}\t 나이 : {1}\t 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")
