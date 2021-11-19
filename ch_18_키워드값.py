
# @Date       : 21.11.18(목) 12:24
# @Author     : ymkim
# @Contents   : 키워드값 실습

def profile(name, age, main_lang) :
    print(name, age, main_lang)

# 순서가 바뀌는줄 알았는데, 순서는 안 바뀌는 것 같음
profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = "25", name = "김영민")
