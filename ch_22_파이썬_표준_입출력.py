# @Date       : 21.11.18(목) 14:05
# @Author     : ymkim
# @Contents   : 표준 입출력

import sys

'''
1. sep
2. file
3. ljsut
4. rjust
5. zfill
'''

# print("Python", "Java")
# print("Python", "Java", sep = ",")
# print("Python", "Java", sep = " vs ")
# print("Python", "Java", sep = ",", end = "?")
# print("무엇이 더 재밌을까요?")

# print()

# print("Python", "Java", file = sys.stdout) # 표준 출력
# print("Python", "Java", file = sys.stderr) # 표준 에러

scores = {
    "수학" : 0,
    "영어" : 50,
    "코딩" : 100
}

# Map Iterator
# for key, value in scores.items() :
#     print(key.ljust(4, str(value).rjust(4), sep=":")

# for num in range(1, 21) :
#     print(str(num).zfill(3))

answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")