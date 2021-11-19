# @Date       : 21.11.17(수) 21:44
# @Author     : ymkim
# @Contents   : 자료구조의 변경

'''
자료구조의 변경
1. api(변수)를 통해 자료구조 변경이 가능하다
2. List => Set, Set => List, tuple => Map....
'''

menu = {"커피", "우유", "주스"} # set(집합)
print(menu, type(menu))

print()

menu = list(menu)
print(menu, type(menu))

print()

menu = tuple(menu)
print(menu, type(menu))

print()

menu = set(menu)
print(menu, type(menu))
