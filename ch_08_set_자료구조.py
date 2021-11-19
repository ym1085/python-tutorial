# @Date       : 21.11.17(수) 21:19
# @Author     : ymkim
# @Contents   : 집합(Set) 실습

'''
집합(Set) 자료구조
1. 중복 허용 x, 순서 역시 보장 x
2. List 자료구조에 비해 속도가 빠름
3. Java에서는 Iterator를 사용해 데이터를 출력

'''

my_set = {1, 2, 3, 3, 3} # 중복 허용 안함
print(my_set)
print()

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

print()

# 교집합 (Java와 Python을 모두 할 수 있는 개발자)
# keyword : intersaction
print(java & python)
print(java.intersection(python))

print()

# 합집합 (Java를 할 수 있거나 Python을 할 수 있는 개발자)
# keyword : union
print(java | python)
print(java.union(python))

print()

# 차집합 (Java는 할 줄 알지만, Python은 할 주 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 까먹었다
java.remove("김태호")
print(java)

print()

# menu_list = {2,3,1,2,3,4,5}
# print(menu_list)

# menu_list_sub = {2,1,3}
# print(menu_list & menu_list_sub)
# print(menu_list.intersection(menu_list_sub))