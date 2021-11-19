# @Date       : 21.11.17(수) 16:47
# @Author     : ymkim
# @Contents   : 문자열 함수 공부

py = "Python is Amazing"   
print(py.lower())                       # 소문자 변환
print(py.upper())                       # 대문자 변환
print(py[0].isupper())                  # 대문자 변환
print(len(py))                          # 길이 반환
print(py.replace("Python", "Java"))     # 문자열 변환

# @ api.index("찾으려는 문자", "위치")
# index() 함수는 찾으려는 값이 없을 경우 오류를 반환
idx = py.index("n")
print("idx = " + str(idx))

idx = py.index("n", idx + 1)
print("idx = " + str(idx)) # 15

# @ api.find("찾으려는 문자")
# find() 함수는 찾으려는 값이 없을 경우 -1을 반환
print("Final = " + py)
print(py.find("Java"))
print(py.replace("Python", "Java").index("Java"))

# @ api.count("찾으려는 문자")
print(py.count("n"))

