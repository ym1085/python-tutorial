# @Date       : 21.11.17(수) 21:12
# @Author     : ymkim
# @Contents   : tuple 실습

'''
참고 사이트 : https://bigdaheta.tistory.com/8

튜플(tuple)과 리스트(list)
1. 리스트는 []로 작성, 튜플은 ()을 이용하여 작성
2. 리스트는 값을 수정할 수 있지만, 튜플은 값을 변경할 수 없다
3. 가장 큰 차이점은 값을 변경할 수 있느냐 없느냐이다

주의사항
1. 튜플이 1개의 데이터만 가질 경우 뒤에 꼭 콤마를 붙여줘야 한다 => Type 문제 발생
'''

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 튜플은 add 기능을 제공하지 않는다

print()

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)