# @Date       : 21.11.18(목) 11:28
# @Author     : ymkim
# @Contents   : 한줄 for문 실습

# 출석번호가 1,2,3,4 앞에 100을 붙이기로함

students = [1, 2, 3, 4, 5]
print(students)

print()

# 한줄 for문

students = [i + 100 for i in students]
print(students)

print()

# 학생 이름을 길이로 변환

students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

students = [i.upper() for i in students]
print(students)