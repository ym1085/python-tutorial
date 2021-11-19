# @Date       : 21.11.17(수) 17:49
# @Author     : ymkim
# @Contents   : 문자열 포맷 함수

# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # %d => 정수값
print("나는 %s을 좋아해요." % "파이썬") # %s => 문자열
print("Apple 은 %c로 시작해요." % "A") # %c => 문자
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 여러개 사용

print

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨강"))

# 방법 4 파이썬 3.6 이상 버전부터 사용가능
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")